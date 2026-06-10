import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：gethostbyaddr -> getxyDataEnt -> WSALookupServiceBeginA -> NtDeviceIoControlFile
_xperf_mark("gethostbyaddr_BEGIN")
result = socket.gethostbyaddr("127.0.0.1")
_xperf_mark("gethostbyaddr_END")
