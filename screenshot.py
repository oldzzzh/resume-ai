
import socket, json
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(30)
sock.connect(("localhost", 9876))
ss_path = "C:\\Users\\18579\\Documents\\一个创意程序\\cup_screenshot.png"
cmd = json.dumps({"type": "get_viewport_screenshot", "params": {"max_size": 1200, "filepath": ss_path, "format": "png"}})
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
r = json.loads(b"".join(chunks).decode())
sock.close()
print(json.dumps(r, indent=2, ensure_ascii=False))
