
import bpy, math, random, bmesh

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

R = 3.2
H = 7.2
WALL = 0.13
MTN_H = 0.6

# 1. Glass body
bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=R, depth=H, location=(0, 0, H/2))
glass = bpy.context.active_object
glass.name = "GlassBody"
bpy.ops.object.shade_smooth()

# 2. Mountain mesh (grid displaced)
bpy.ops.mesh.primitive_grid_add(x_subdivisions=50, y_subdivisions=50, size=(R*2-0.4))
mtn = bpy.context.active_object
mtn.name = "Mountain"
mtn.location.z = 0.01

# Displace vertices to make mountain
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
bm = bmesh.from_edit_mesh(mtn.data)
mr = max(math.sqrt(v.co.x**2+v.co.y**2) for v in bm.verts)

for v in bm.verts:
    d = math.sqrt(v.co.x**2 + v.co.y**2)
    nd = d / mr if mr > 0 else 1
    h = 0
    if nd < 0.4:
        h = MTN_H * (1 - nd * 2.5) + math.sin(v.co.x*6)*math.cos(v.co.y*5)*0.08 + math.sin(v.co.x*12+v.co.y*8)*0.04
    elif nd < 0.7:
        h = MTN_H * 0.25 * (1 - (nd-0.4)*3.3) + math.sin(v.co.x*4+v.co.y*3)*0.03
    else:
        h = MTN_H * 0.05 * max(0, 1 - (nd-0.7)*3.3)
    v.co.z = max(0, h)

bmesh.update_edit_mesh(mtn.data)
bpy.ops.object.mode_set(mode="OBJECT")
bpy.ops.object.shade_smooth()

# 3. Boolean union
bpy.ops.object.select_all(action="DESELECT")
glass.select_set(True)
mtn.select_set(True)
bpy.context.view_layer.objects.active = glass
mb = glass.modifiers.new(name="JoinMtn", type="BOOLEAN")
mb.operation = "UNION"
mb.object = mtn
bpy.ops.object.modifier_apply(modifier="JoinMtn")
bpy.data.objects.remove(mtn, do_unlink=True)

# 4. Solidify
ms = glass.modifiers.new(name="Wall", type="SOLIDIFY")
ms.thickness = WALL
ms.offset = -1.0
ms.use_even_offset = True

# 5. Subsurf
mss = glass.modifiers.new(name="Smooth", type="SUBSURF")
mss.levels = 2
mss.render_levels = 2

# 6. Glass material
mat = bpy.data.materials.new(name="Glass_Mat")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.85, 0.9, 0.95, 1)
bsdf.inputs["Roughness"].default_value = 0.01
bsdf.inputs["Transmission Weight"].default_value = 0.92
bsdf.inputs["IOR"].default_value = 1.45
glass.data.materials.append(mat)

# 7. Scene setup - camera, lights
cam = bpy.data.objects.get("Camera")
if cam:
    cam.location = (8, -5, 4)
    cam.rotation_euler = (1.2, 0, 0.9)

# Main light
light = bpy.data.objects.get("Light")
if light:
    light.location = (5, 3, 8)
    light.data.energy = 2000

# Studio lighting
for pos, en in [((-4, 4, 6), 800), ((3, -5, 4), 600), ((0, 0, 10), 500)]:
    ld = bpy.data.lights.new(name=f"Light_{pos[0]}", type="AREA")
    lo = bpy.data.objects.new(name=f"Light_{pos[0]}", object_data=ld)
    bpy.context.scene.collection.objects.link(lo)
    lo.location = pos
    ld.energy = en

# World
world = bpy.data.worlds[0]
world.use_nodes = True
bg = world.node_tree.nodes.get("Background")
if bg:
    bg.inputs["Strength"].default_value = 0.5
    bg.inputs["Color"].default_value = (0.1, 0.12, 0.15, 1)

# Viewport shading
for area in bpy.context.screen.areas:
    if area.type == "VIEW_3D":
        for space in area.spaces:
            if space.type == "VIEW_3D":
                space.shading.type = "MATERIAL"

print("Mountain glass created!")
print("Inner volume ~200ml")
