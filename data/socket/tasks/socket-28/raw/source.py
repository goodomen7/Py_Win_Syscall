import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 0))

# 触发：WSAIoctl -> WSPIoctl -> SetSocketInformation
#        -> NtDeviceIoControlFile(IOCTL_AFD_SET_INFO) [FIONBIO路径]
#   或   -> NtDeviceIoControlFile(IOCTL_AFD_GET_INFO) [FIONREAD路径]
_xperf_mark("ioctl_SIO_KEEPALIVE_VALS_BEGIN")
s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
_xperf_mark("ioctl_SIO_KEEPALIVE_VALS_END")

s.close()
