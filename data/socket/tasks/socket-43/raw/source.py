import socket, os
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 触发：WSADuplicateSocketW -> WSPDuplicateSocket -> NtDuplicateObject
_xperf_mark("share_BEGIN")
info_bytes = s.share(os.getpid())
_xperf_mark("share_END")

s.close()
