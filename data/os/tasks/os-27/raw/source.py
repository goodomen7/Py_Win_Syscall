import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# os.listmounts 接受卷 GUID 路径（\\?\Volume{...}\），不是盘符路径。
# 先用 os.listvolumes() 取第一个卷路径再传入。
volume = next(os.listvolumes())

# 触发：NtFsControlFile
_xperf_mark("os_listmounts__NtFsControlFile__BEGIN")
mounts = os.listmounts(volume)
_xperf_mark("os_listmounts__NtFsControlFile__END")