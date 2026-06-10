import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 条件A：SOL_SOCKET 常用选项 — 直接读 SharedData 内存，无系统调用
val_type = s.getsockopt(socket.SOL_SOCKET, socket.SO_TYPE)  # 无系统调用

# 条件B：IPPROTO_TCP 选项 — 触发 WSHGetSocketInformation -> NtDeviceIoControlFile
_xperf_mark("getsockopt_IPPROTO_TCP_BEGIN")
val_nodelay = s.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)
_xperf_mark("getsockopt_IPPROTO_TCP_END")

s.close()
