import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

import os
src = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
info = src.share(os.getpid())   # 获取 WSAPROTOCOL_INFOW bytes
# 触发：WSASocketW(FROM_PROTOCOL_INFO) -> NtCreateFile(\Device\Afd\Endpoint)
_xperf_mark("fromshare_BEGIN")
s2 = socket.fromshare(info)
_xperf_mark("fromshare_END")
s2.close()
src.close()
