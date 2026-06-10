import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

r, w = os.pipe()
os.close(w)  # 关闭写端，保留读端备用

# 触发条件：有效 fd
# 触发：NtClose
_xperf_mark("os_close__NtClose__BEGIN")
os.close(r)
_xperf_mark("os_close__NtClose__END")
