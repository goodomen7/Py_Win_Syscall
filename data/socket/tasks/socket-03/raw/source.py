import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：getaddrinfo(DNS查询) + WSASocketW(NtCreateFile) + connect(NtDeviceIoControlFile IOCTL_AFD_CONNECT)
_xperf_mark("create_connection_BEGIN")
conn = socket.create_connection(("127.0.0.1", 80), timeout=2)
_xperf_mark("create_connection_END")
conn.close()
