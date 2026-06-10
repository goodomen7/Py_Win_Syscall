import socket, threading
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]

def _client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", port))
    c.close()

t = threading.Thread(target=_client)
t.start()

_xperf_mark("accept_BEGIN")
conn, addr = srv.accept()
_xperf_mark("accept_END")

conn.close()
t.join()
srv.close()
