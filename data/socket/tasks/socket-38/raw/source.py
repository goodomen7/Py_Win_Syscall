import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 触发：SetHandleInformation -> NtQueryObject + NtSetInformationObject
_xperf_mark("set_inheritable_BEGIN")
s.set_inheritable(True)
_xperf_mark("set_inheritable_END")

s.close()
