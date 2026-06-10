import socket, threading, tempfile, os
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# Windows 无 os.sendfile，退化为 read+send 循环
# 触发：多次 send -> WSPSend -> NtDeviceIoControlFile(IOCTL_AFD_SEND)

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]

t = threading.Thread(target=lambda: srv.accept()[0].close())
t.start()

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))

with tempfile.NamedTemporaryFile(delete=False) as f:
    f.write(b"x" * 4096)
    fname = f.name

with open(fname, "rb") as f:
    _xperf_mark("sendfile_BEGIN")
    c.sendfile(f)
    _xperf_mark("sendfile_END")
