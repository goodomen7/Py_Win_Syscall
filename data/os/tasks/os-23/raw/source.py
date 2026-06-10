import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.close()

# lchmod 作用于符号链接自身（不跟随链接）
# 触发：NtOpenFile + NtSetInformationFile
_xperf_mark("os_lchmod__NtOpenFile_NtSetInformationFile__BEGIN")
os.lchmod(tmp.name, 0o644)
_xperf_mark("os_lchmod__NtOpenFile_NtSetInformationFile__END")

os.unlink(tmp.name)
