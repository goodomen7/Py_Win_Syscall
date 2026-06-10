import socket, threading
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 0))
port = s.getsockname()[1]
buf = bytearray(1024)

def _sender():
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender.sendto(b"ping", ("127.0.0.1", port))
    sender.close()

t = threading.Thread(target=_sender)
t.start()

# 触发：recvfrom_into -> sock_recvfrom_guts -> recvfrom
#        -> WSPRecvFrom -> NtDeviceIoControlFile(IOCTL_AFD_RECV_DATAGRAM)
_xperf_mark("recvfrom_into_BEGIN")
nbytes, addr = s.recvfrom_into(buf)
_xperf_mark("recvfrom_into_END")

t.join()
s.close()
