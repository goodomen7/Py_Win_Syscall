import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmpdir = tempfile.gettempdir()

def _make_file(name, content=b"data"):
    p = os.path.join(tmpdir, name)
    with open(p, "wb") as f: f.write(content)
    return p

# ── 场景 A：目标不存在
# 触发：NtOpenFile + NtCreateFile + NtSetInformationFile
src_a = _make_file("_xperf_rename_src_a.tmp")
dst_a = os.path.join(tmpdir, "_xperf_rename_dst_a.tmp")

_xperf_mark("os_rename__no_dst__NtOpenFile_NtCreateFile_NtSetInformationFile__BEGIN")
os.rename(src_a, dst_a)
_xperf_mark("os_rename__no_dst__NtOpenFile_NtCreateFile_NtSetInformationFile__END")
os.unlink(dst_a)

# ── 场景 B：目标已存在，rename 语义（Windows 上会抛 FileExistsError）
#   内部仍先走 NtOpenFile 探查目标，再 NtClose；异常由上层抛出。
# 触发：NtOpenFile + NtClose
src_b = _make_file("_xperf_rename_src_b.tmp")
dst_b = _make_file("_xperf_rename_dst_b.tmp")

_xperf_mark("os_rename__dst_exists_rename__NtOpenFile_NtClose__BEGIN")
try:
    os.rename(src_b, dst_b)
except FileExistsError:
    pass
_xperf_mark("os_rename__dst_exists_rename__NtOpenFile_NtClose__END")
os.unlink(src_b)
os.unlink(dst_b)

# ── 场景 C：目标已存在，replace 语义（os.replace 原子覆盖）
# 触发：NtOpenFile + NtCreateFile + NtSetInformationFile
src_c = _make_file("_xperf_rename_src_c.tmp")
dst_c = _make_file("_xperf_rename_dst_c.tmp")

_xperf_mark("os_rename__dst_exists_replace__NtOpenFile_NtCreateFile_NtSetInformationFile__BEGIN")
os.replace(src_c, dst_c)
_xperf_mark("os_rename__dst_exists_replace__NtOpenFile_NtCreateFile_NtSetInformationFile__END")
os.unlink(dst_c)
