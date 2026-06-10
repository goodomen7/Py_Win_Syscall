import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

src = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fd = src.fileno()
# 触发：WSADuplicateSocketW + WSASocketW(NtCreateFile)
_xperf_mark("fromfd_BEGIN")
s2 = socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)
_xperf_mark("fromfd_END")
s2.close()
src.close()
