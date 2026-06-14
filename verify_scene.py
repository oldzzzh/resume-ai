
import socket, json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect(("localhost", 9876))
s.sendall(json.dumps({"type": "get_scene_info", "params": {}}).encode())
ch = []
while True:
    try:
        ck = s.recv(65536)
        if not ck:
            break
        ch.append(ck)
        json.loads(b"".join(ch).decode())
        break
    except json.JSONDecodeError:
        continue
    except socket.timeout:
        break
r = json.loads(b"".join(ch).decode())
s.close()
d = r.get("result", r)
for o in d.get("objects", []):
    print(f'  {o["name"]:15s} ({o["type"]:8s}) @ {o["location"]}')
print(f'Total: {d["object_count"]} objects, {d["materials_count"]} materials')
