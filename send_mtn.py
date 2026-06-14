
import socket, json
with open(r"C:\Users\18579\Documents\一个创意程序\mountain_glass.py", "r") as f:
    code = f.read()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(60)
sock.connect(("localhost", 9876))
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
r = json.loads(b"".join(chunks).decode())
sock.close()
print(json.dumps(r, indent=2, ensure_ascii=False))
