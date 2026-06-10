import socket, threading
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]

def _server():
    conn, _ = srv.accept()
    conn.sendall(b"hello")
    conn.close()

t = threading.Thread(target=_server)
t.start()

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))

# 触发：recv -> WSPRecv -> NtDeviceIoControlFile(IOCTL_AFD_RECV)
_xperf_mark("recv_BEGIN")
data = c.recv(1024)
_xperf_mark("recv_END")

c.close()
t.join()
srv.close()
