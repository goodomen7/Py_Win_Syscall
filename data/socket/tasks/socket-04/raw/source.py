import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：WSASocketW(NtCreateFile) + bind(IOCTL_AFD_BIND) + listen(IOCTL_AFD_START_LISTEN)
_xperf_mark("create_server_BEGIN")
srv = socket.create_server(("127.0.0.1", 0))
_xperf_mark("create_server_END")
srv.close()
