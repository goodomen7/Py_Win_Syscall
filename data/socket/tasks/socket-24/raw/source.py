import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 触发：GetHandleInformation -> NtQueryObject(ObjectHandleFlagInformation)
_xperf_mark("get_inheritable_BEGIN")
flag = s.get_inheritable()
_xperf_mark("get_inheritable_END")

s.close()
