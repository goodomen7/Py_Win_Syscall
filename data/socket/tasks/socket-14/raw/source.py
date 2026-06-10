import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：getservbyname -> getxyDataEnt -> WSALookupServiceBeginA -> NtDeviceIoControlFile
_xperf_mark("getservbyname_BEGIN")
port = socket.getservbyname("http")
_xperf_mark("getservbyname_END")
