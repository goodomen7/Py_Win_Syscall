import mmap
import os

m_anon = mmap.mmap(-1, 4096)
m_anon.close()

_m_resize = mmap.mmap(-1, 4096)
_m_resize.resize(8192)

tmp_file = "tmp.bin"
with open(tmp_file, "wb") as f:
    f.write(b"\x00" * 1024)

with open(tmp_file, "r+b") as f:
    with mmap.mmap(f.fileno(), 0) as m:
        size = m.size()
        print(f"文件映射大小: {size}")

if os.path.exists(tmp_file):
    os.remove(tmp_file)

_m_resize.close()