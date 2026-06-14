
import bpy, math
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.mesh.primitive_monkey_add(size=2, location=(0, 0, 0))
bpy.ops.mesh.primitive_torus_add(major_radius=2.5, minor_radius=0.15, location=(0, 0, 2.5))
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.8, location=(3, 0, 0.5))
bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=2, location=(-3, 0, 0.5))
# Create materials with colors
mat_red = bpy.data.materials.new(name="Red_Mat")
mat_red.use_nodes = True
mat_red.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.1, 0.1, 1.0)
mat_blue = bpy.data.materials.new(name="Blue_Mat")
mat_blue.use_nodes = True
mat_blue.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.1, 0.2, 0.8, 1.0)
mat_gold = bpy.data.materials.new(name="Gold_Mat")
mat_gold.use_nodes = True
mat_gold.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.6, 0.1, 1.0)
mat_gold.node_tree.nodes["Principled BSDF"].inputs[4].default_value = 0.8
# Assign materials
for obj in bpy.data.objects:
    if obj.type == "MESH":
        if "Monkey" in obj.name:
            obj.data.materials.append(mat_red)
        elif "Sphere" in obj.name:
            obj.data.materials.append(mat_blue)
        elif "Cylinder" in obj.name or obj.name.startswith("Cylinder"):
            obj.data.materials.append(mat_gold)
        elif "Torus" in obj.name:
            obj.data.materials.append(mat_gold)
print("Done!")
