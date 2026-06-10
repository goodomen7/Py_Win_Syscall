import socket, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 必须先 connect，才有 TdiConnectionHandle
# 设置 SO_LINGER 以强制走 IOCTL_AFD_DISCONNECT 分支
linger = struct.pack("hh", 1, 0)   # l_onoff=1, l_linger=0
s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, linger)

_xperf_mark("close_BEGIN")
s.close()
_xperf_mark("close_END")