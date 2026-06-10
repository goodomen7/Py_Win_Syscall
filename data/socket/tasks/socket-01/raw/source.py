import socket

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：WSASocketW -> NtCreateFile(\Device\Afd\Endpoint)
_xperf_mark("socket_BEGIN")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_xperf_mark("socket_END")

s.close()
