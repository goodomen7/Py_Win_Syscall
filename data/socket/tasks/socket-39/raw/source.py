import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 触发：ioctlsocket(FIONBIO) -> WSAIoctl -> WSPIoctl(FIONBIO)
#        -> SetSocketInformation(AFD_INFO_BLOCKING_MODE)
#        -> NtDeviceIoControlFile(IOCTL_AFD_SET_INFO)
_xperf_mark("setblocking_False_BEGIN")
s.setblocking(False)          # 设为非阻塞 → 触发 ioctlsocket
_xperf_mark("setblocking_False_END")

_xperf_mark("setblocking_True_BEGIN")
s.setblocking(True)           # 设回阻塞 → 再次触发 ioctlsocket
_xperf_mark("setblocking_True_END")

s.close()
