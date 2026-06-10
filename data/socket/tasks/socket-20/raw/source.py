import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 触发：bind -> WSPBind -> NtCreateEvent + NtDeviceIoControlFile(IOCTL_AFD_BIND)
_xperf_mark("bind_BEGIN")
s.bind(("127.0.0.1", 0))
_xperf_mark("bind_END")

s.close()
