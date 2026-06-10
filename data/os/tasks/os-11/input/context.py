import os
import tempfile
import shutil
import msvcrt


for i in range(200):
    os.environ[f"_FILL_{i}"] = "x" * 100

for i in range(200):
    os.environ[f"_FILL_{i}"] = "x" * 100

try:
    for i in range(200):
        del os.environ[f"_FILL_{i}"]
    os.environ["_TRIGGER_EXPAND"] = "z" * (32767 - len("_TRIGGER_EXPAND") - 1)
except Exception as e:
    print(f"error: {e}")


_orig = os.getcwd()
os.chdir("C:\\")
os.chdir(_orig)


ppid = os.getppid()


os.putenv("BIGENV", "A" * (1024 * 1024))


r, w = os.pipe()
os.close(w)
os.close(r)


tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()
os.fchmod(fd, 0o644)
tmp.close()
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()
os.fstat(fd)
tmp.close()
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"data to sync")
fd = tmp.fileno()
os.fsync(fd)
tmp.close()
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"x" * 1024)
fd = tmp.fileno()
os.ftruncate(fd, 512)
tmp.close()
os.unlink(tmp.name)


r, w = os.pipe()
os.set_blocking(r, False)
os.close(r)
os.close(w)


tmp_path = tempfile.mktemp(suffix=".tmp")
fd = os.open(tmp_path, os.O_CREAT | os.O_WRONLY)
os.close(fd)
os.unlink(tmp_path)


r, w = os.pipe()
os.close(r)
os.close(w)


tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"hello world")
tmp.close()
fd = os.open(tmp.name, os.O_RDONLY)
data = os.read(fd, 11)
os.close(fd)
os.unlink(tmp.name)


os.readlink("test_link.txt")


r, w = os.pipe()
os.set_blocking(r, True)
os.close(r)
os.close(w)


tmp_path = tempfile.mktemp(suffix=".tmp")
fd = os.open(tmp_path, os.O_CREAT | os.O_WRONLY)
os.write(fd, b"hello world")
os.close(fd)
os.unlink(tmp_path)


tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()
result = os.get_inheritable(fd)
tmp.close()
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()
os.set_inheritable(fd, True)
tmp.close()
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()
handle = msvcrt.get_osfhandle(fd)
result = os.get_handle_inheritable(handle)
tmp.close()
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()
handle = msvcrt.get_osfhandle(fd)
os.set_handle_inheritable(handle, True)
tmp.close()
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.close()
os.access(tmp.name, os.R_OK)
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.close()
os.chmod(tmp.name, 0o644)
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.close()
os.lchmod(tmp.name, 0o644)
os.unlink(tmp.name)


tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"link source")
tmp.close()
link_path = tmp.name + ".hardlink"
os.link(tmp.name, link_path)
os.unlink(link_path)
os.unlink(tmp.name)


tmpdir = tempfile.mkdtemp()
os.listdir(tmpdir)
os.rmdir(tmpdir)


drives = os.listdrives()


volume = next(os.listvolumes())
mounts = os.listmounts(volume)


volumes = list(os.listvolumes())


tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.close()
os.lstat(tmp.name)
os.unlink(tmp.name)


new_dir = os.path.join(tempfile.gettempdir(), "_xperf_mkdir_test")
os.mkdir(new_dir)
os.rmdir(new_dir)


nested = os.path.join(tempfile.gettempdir(), "_xperf_makedirs_a", "b", "c")
os.makedirs(nested)
shutil.rmtree(os.path.join(tempfile.gettempdir(), "_xperf_makedirs_a"))


def _make_file(name, content=b"data"):
    p = os.path.join(tempfile.gettempdir(), name)
    with open(p, "wb") as f:
        f.write(content)
    return p

src_a = _make_file("_xperf_rename_src_a.tmp")
dst_a = os.path.join(tempfile.gettempdir(), "_xperf_rename_dst_a.tmp")
os.rename(src_a, dst_a)
os.unlink(dst_a)

src_b = _make_file("_xperf_rename_src_b.tmp")
dst_b = _make_file("_xperf_rename_dst_b.tmp")
try:
    os.rename(src_b, dst_b)
except FileExistsError:
    pass
os.unlink(src_b)
os.unlink(dst_b)

src_c = _make_file("_xperf_rename_src_c.tmp")
dst_c = _make_file("_xperf_rename_dst_c.tmp")
os.replace(src_c, dst_c)
os.unlink(dst_c)


open("src.txt", "w").close()
open("dst.txt", "w").close()
os.replace("src.txt", "dst.txt")


os.mkdir("empty_dir")
os.rmdir("empty_dir")


with os.scandir(".") as it:
    for entry in it:
        pass


open("stat_target.txt", "w").close()
os.stat("stat_target.txt")
os.unlink("stat_target.txt")
