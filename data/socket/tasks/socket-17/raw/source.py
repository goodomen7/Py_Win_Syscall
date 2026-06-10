import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 取一个真实接口名（如 "以太网" 或 "Ethernet"）
iface_name = socket.if_nameindex()[0][1]

# 触发：if_nametoindex(iphlpapi) -> ZwCreateFile(\Device\Tcp)(NtCreateFile)
#        + DeviceIoControl(IOCTL_TCP_QUERY_INFORMATION_EX)(NtDeviceIoControlFile)
_xperf_mark("if_nametoindex_BEGIN")
idx = socket.if_nametoindex(iface_name)
_xperf_mark("if_nametoindex_END")
