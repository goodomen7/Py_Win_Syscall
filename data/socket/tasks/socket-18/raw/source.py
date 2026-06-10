import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 取一个真实接口索引
iface_idx = socket.if_nameindex()[0][0]

# 触发：if_indextoname(iphlpapi) -> ZwCreateFile(\Device\Tcp)(NtCreateFile)
#        + DeviceIoControl(IOCTL_TCP_QUERY_INFORMATION_EX)(NtDeviceIoControlFile)
_xperf_mark("if_indextoname_BEGIN")
name = socket.if_indextoname(iface_idx)
_xperf_mark("if_indextoname_END")
