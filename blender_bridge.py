"""Blenger Bridge - Connect Codex to Blender via TCP socket"""
import socket, json, sys, os

H = os.environ.get("BLENDER_HOST", "localhost")
P = int(os.environ.get("BLENDER_PORT", "9876"))

def sc(cmd, p=None):
    if p is None: p={}
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(60)
    try:
        s.connect((H,P))
        s.sendall(json.dumps({"type": cmd, "params": p}).encode())
        ch=[]
        while True:
            try:
                ck=s.recv(65536)
                if not ck: break
                ch.append(ck)
                json.loads(b"".join(ch).decode())
                return json.loads(b"".join(ch).decode())
            except json.JSONDecodeError: continue
            except socket.timeout: break
        if ch: return json.loads(b"".join(ch).decode())
        return {"status":"error","message":"no response"}
    except ConnectionRefusedError: return {"status":"error","message":"Blender not running"}
    except Exception as e: return {"status":"error","message":str(e)}
    finally: s.close()

def pr(res):
    if res.get("status")=="error":
        print("ERROR:",res.get("message",""))
        sys.exit(1)
    d=res.get("result",res)
    print(json.dumps(d,indent=2,ensure_ascii=False))

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: py bridge.py cmd [params]")
        sys.exit(1)
    cmd=sys.argv[1]
    params={}
    if len(sys.argv)>2:
        try: params=json.loads(sys.argv[2])
        except: params={"code":sys.argv[2]} if cmd=="execute_code" else {}
    pr(sc(cmd,params))