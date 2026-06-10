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
c.connect(("127.0.0.1", port))

# 触发：send -> sock_send_impl -> send(Win32) -> WSPSend
#        -> NtDeviceIoControlFile(IOCTL_AFD_SEND)
_xperf_mark("send_BEGIN")
c.send(b"hello")
_xperf_mark("send_END")

c.close()
t.join()
srv.close()
