
import bpy, math

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

# 1. Cup body
bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1.0, depth=1.4, location=(0, 0, 0.7))
cup = bpy.context.active_object
cup.name = "CupBody"
mod = cup.modifiers.new(name="Thickness", type="SOLIDIFY")
mod.thickness = 0.08
mod.offset = -1.0
mod2 = cup.modifiers.new(name="Smooth", type="SUBSURF")
mod2.levels = 2

# 2. Handle
bpy.ops.mesh.primitive_torus_add(major_radius=0.6, minor_radius=0.07, location=(1.0, 0, 0.9), rotation=(0, 1.5708, 0))
handle = bpy.context.active_object
handle.name = "Handle"

# 3. Coffee surface
bpy.ops.mesh.primitive_circle_add(vertices=32, radius=0.87, location=(0, 0, 1.32))
coffee = bpy.context.active_object
coffee.name = "CoffeeSurface"

# 4. Base rim
bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1.04, depth=0.04, location=(0, 0, 0.02))
base = bpy.context.active_object
base.name = "BaseRim"

# Materials using input names
mat_c = bpy.data.materials.new(name="Ceramic")
mat_c.use_nodes = True
bsdf = mat_c.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.92, 0.92, 0.97, 1)
bsdf.inputs["Roughness"].default_value = 0.15
if "Specular IOR Level" in bsdf.inputs:
    bsdf.inputs["Specular IOR Level"].default_value = 0.5

mat_cf = bpy.data.materials.new(name="Coffee")
mat_cf.use_nodes = True
bsdf2 = mat_cf.node_tree.nodes["Principled BSDF"]
bsdf2.inputs["Base Color"].default_value = (0.18, 0.08, 0.03, 1)
bsdf2.inputs["Roughness"].default_value = 0.8

for obj in [cup, handle, base]:
    obj.data.materials.append(mat_c)
coffee.data.materials.append(mat_cf)

for obj in [cup, handle, base, coffee]:
    obj.select_set(True)
bpy.ops.object.shade_smooth()
bpy.ops.object.select_all(action="DESELECT")
print("Coffee cup created!")
