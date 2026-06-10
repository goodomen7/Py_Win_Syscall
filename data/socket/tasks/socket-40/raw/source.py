import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 初始为阻塞模式 (timeout=-1)

# 条件A：设置超时值（从阻塞→非阻塞fd）
# 触发：ioctlsocket(FIONBIO) -> NtDeviceIoControlFile(IOCTL_AFD_SET_INFO)
_xperf_mark("settimeout_nonzero_BEGIN")
s.settimeout(5.0)             # 触发 ioctlsocket
_xperf_mark("settimeout_nonzero_END")

# 条件B：改变超时值但 fd 已是非阻塞，无模式切换 → 仅写内存，无系统调用
s.settimeout(3.0)             # 无系统调用（fd 已是非阻塞）

# 条件C：设回 None（非阻塞→阻塞）
# 触发：ioctlsocket(FIONBIO) -> NtDeviceIoControlFile(IOCTL_AFD_SET_INFO)
_xperf_mark("settimeout_None_BEGIN")
s.settimeout(None)            # 触发 ioctlsocket
_xperf_mark("settimeout_None_END")

s.close()
