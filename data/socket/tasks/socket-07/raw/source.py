import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：getaddrinfo -> GetAddrInfoW -> WSALookupServiceBeginW -> NSPLookupServiceBegin -> NtDeviceIoControlFile
_xperf_mark("getaddrinfo_BEGIN")
results = socket.getaddrinfo("localhost", 80, socket.AF_INET, socket.SOCK_STREAM)
_xperf_mark("getaddrinfo_END")
