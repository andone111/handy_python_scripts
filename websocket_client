import ssl
import threading
import websocket
import sys

ws = websocket.create_connection(
    "SERVER",
    sslopt={"cert_reqs": ssl.CERT_NONE}
)

def receive():
    while True:
        try:
            data = ws.recv()
            print(data, end="", flush=True)
        except Exception as e:
            print(f"\n[recv] {e}", file=sys.stderr)
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    try:
        ws.send(input() + "\n")
    except (EOFError, KeyboardInterrupt):
        break
