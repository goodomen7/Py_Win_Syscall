import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 0))

# 触发：getsockname -> WSPGetSockName -> NtDeviceIoControlFile(IOCTL_AFD_GET_SOCK_NAME)
_xperf_mark("getsockname_BEGIN")
addr = s.getsockname()
_xperf_mark("getsockname_END")

s.close()
