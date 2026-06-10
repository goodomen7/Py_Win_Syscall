import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：getservbyport -> getxyDataEnt -> WSALookupServiceBeginA -> NtDeviceIoControlFile
_xperf_mark("getservbyport_BEGIN")
name = socket.getservbyport(80)
_xperf_mark("getservbyport_END")
