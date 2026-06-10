import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：getaddrinfo(NtDeviceIoControlFile) + getnameinfo -> GetNameInfoW
#        -> WSALookupServiceBeginW -> NtDeviceIoControlFile
_xperf_mark("getnameinfo_BEGIN")
result = socket.getnameinfo(("127.0.0.1", 80), 0)
_xperf_mark("getnameinfo_END")
