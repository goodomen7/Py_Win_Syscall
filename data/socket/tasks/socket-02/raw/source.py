import socket

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：WSASocketW x2 -> NtCreateFile(\Device\Afd\Endpoint) x2
_xperf_mark("socketpair_BEGIN")
s1, s2 = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)
_xperf_mark("socketpair_END")

s1.close()
s2.close()
