import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"link source")
tmp.close()

link_path = tmp.name + ".hardlink"

# 触发：NtSetInformationFile（创建硬链接）
_xperf_mark("os_link__NtSetInformationFile__BEGIN")
os.link(tmp.name, link_path)
_xperf_mark("os_link__NtSetInformationFile__END")

os.unlink(link_path)
os.unlink(tmp.name)
