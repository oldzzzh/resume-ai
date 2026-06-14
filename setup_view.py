
import socket, json
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
sock.connect(("localhost", 9876))

# First set up viewport and lighting
code = '''
import bpy

# Set viewport to smooth shading
for area in bpy.context.screen.areas:
    if area.type == "VIEW_3D":
        for space in area.spaces:
            if space.type == "VIEW_3D":
                space.shading.type = "MATERIAL"

# Set up camera
cam = bpy.data.objects.get("Camera")
if cam:
    cam.location = (3.5, -3.0, 2.5)
    cam.rotation_euler = (1.1, 0, 0.8)

# Add a nice environment light
world = bpy.data.worlds[0]
world.use_nodes = True
bg = world.node_tree.nodes.get("Background")
if bg:
    bg.inputs["Strength"].default_value = 2.0
    bg.inputs["Color"].default_value = (0.8, 0.85, 1.0, 1)

# Light setup
light = bpy.data.objects.get("Light")
if light:
    light.location = (3, 2, 5)
    light.data.energy = 1000

# Add fill light
fill_data = bpy.data.lights.new(name="FillLight", type="AREA")
fill = bpy.data.objects.new(name="FillLight", object_data=fill_data)
bpy.context.scene.collection.objects.link(fill)
fill.location = (-3, 2, 3)
fill.data.energy = 300

print("View ready")
'''

cmd = json.dumps({"type": "execute_code", "params": {"code": code}})
sock.sendall(cmd.encode())
chunks = []
while True:
    try:
        ck = sock.recv(65536)
        if not ck: break
        chunks.append(ck)
        json.loads(b"".join(chunks).decode())
        break
    except json.JSONDecodeError: continue
    except socket.timeout: break
result = json.loads(b"".join(chunks).decode())
sock.close()
print(json.dumps(result, indent=2, ensure_ascii=False))
