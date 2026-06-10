import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# os.listvolumes() 为 Python 3.12+ Windows 专有函数
# 触发：NtFsControlFile
_xperf_mark("os_listvolumes__NtFsControlFile__BEGIN")
volumes = list(os.listvolumes())
_xperf_mark("os_listvolumes__NtFsControlFile__END")
