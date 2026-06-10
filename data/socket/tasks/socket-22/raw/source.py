import socket, threading
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]

t = threading.Thread(target=lambda: srv.accept()[0].close())
t.start()

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 触发：connect -> WSPConnect
#   -> NtCreateEvent
#   -> WSPBind(隐式) -> NtDeviceIoControlFile(IOCTL_AFD_BIND)
#   -> NtDeviceIoControlFile(IOCTL_AFD_CONNECT)
_xperf_mark("connect_BEGIN")
c.connect(("127.0.0.1", port))
_xperf_mark("connect_END")

c.close()
t.join()
srv.close()
