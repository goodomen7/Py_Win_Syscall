import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：GetIfTable2Ex -> NtDeviceIoControlFile(IOCTL_TCP_QUERY_INFORMATION_EX)
_xperf_mark("if_nameindex_BEGIN")
result = socket.if_nameindex()
_xperf_mark("if_nameindex_END")
