import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 0))

# 触发：listen -> WSPListen -> NtCreateEvent + NtDeviceIoControlFile(IOCTL_AFD_START_LISTEN)
_xperf_mark("listen_BEGIN")
s.listen(5)
_xperf_mark("listen_END")

s.close()
