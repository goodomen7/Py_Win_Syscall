import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 条件A：SO_REUSEADDR (SOL_SOCKET) — 写 SharedData 内存，无系统调用
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 无系统调用

# 条件B：TCP_NODELAY (IPPROTO_TCP) — 触发 WSHSetSocketInformation
#         -> DeviceIoControl(IOCTL_TCP_SET_INFORMATION_EX)
#         -> NtDeviceIoControlFile
_xperf_mark("setsockopt_TCP_NODELAY_BEGIN")
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
_xperf_mark("setsockopt_TCP_NODELAY_END")

s.close()
