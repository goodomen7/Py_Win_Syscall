import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：getaddrinfo -> WSALookupServiceBeginA -> NtDeviceIoControlFile(DNS NSP)
_xperf_mark("gethostbyname_BEGIN")
ip = socket.gethostbyname("localhost")
_xperf_mark("gethostbyname_END")
