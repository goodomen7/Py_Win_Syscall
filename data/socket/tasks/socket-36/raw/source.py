import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 触发：sendto -> sock_sendto_impl -> sendto(Win32) -> WSPSendTo
#        -> NtDeviceIoControlFile(IOCTL_AFD_SEND_DATAGRAM)
_xperf_mark("sendto_BEGIN")
s.sendto(b"ping", ("127.0.0.1", 9))   # port 9 = discard
_xperf_mark("sendto_END")

s.close()
