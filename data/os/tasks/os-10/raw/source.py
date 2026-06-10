import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# os.set_blocking 在 Windows 上只对管道句柄有效；
# 普通文件句柄不支持非阻塞模式设置，会触发 WinError 87。
r, w = os.pipe()

# 触发：NtSetInformationFile
_xperf_mark("os_set_blocking__NtSetInformationFile__BEGIN")
os.set_blocking(r, False)
_xperf_mark("os_set_blocking__NtSetInformationFile__END")

os.close(r)
os.close(w)