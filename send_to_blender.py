
import socket, json

with open(r"C:\Users\18579\Documents\一个创意程序\build_scene.py", "r") as f2:
    code2 = f2.read()

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.settimeout(30)
sock2.connect(("localhost", 9876))
cmd2 = json.dumps({"type": "execute_code", "params": {"code": code2}})
sock2.sendall(cmd2.encode())

chunks2 = []
while True:
    try:
        chunk2 = sock2.recv(65536)
        if not chunk2: break
        chunks2.append(chunk2)
        json.loads(b"".join(chunks2).decode())
        break
    except json.JSONDecodeError:
        continue
    except socket.timeout:
        break

result2 = json.loads(b"".join(chunks2).decode())
sock2.close()
print(json.dumps(result2, indent=2, ensure_ascii=False))
