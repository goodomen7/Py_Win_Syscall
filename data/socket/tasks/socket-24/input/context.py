import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.close()

import socket
s1, s2 = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)
s1.close()
s2.close()

import socket
conn = socket.create_connection(("127.0.0.1", 80), timeout=2)
conn.close()

import socket
srv = socket.create_server(("127.0.0.1", 0))
srv.close()

import socket
src = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fd = src.fileno()
s2 = socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)
s2.close()
src.close()

import socket
import os
src = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
info = src.share(os.getpid())
s2 = socket.fromshare(info)
s2.close()
src.close()

import socket
results = socket.getaddrinfo("localhost", 80, socket.AF_INET, socket.SOCK_STREAM)

import socket
fqdn = socket.getfqdn()

import socket
ip = socket.gethostbyname("localhost")

import socket
name = socket.gethostname()

import socket
result = socket.gethostbyaddr("127.0.0.1")

import socket
result = socket.getnameinfo(("127.0.0.1", 80), 0)

import socket
p = socket.getprotobyname("tcp")

import socket
port = socket.getservbyname("http")

import socket
name = socket.getservbyport(80)

import socket
result = socket.if_nameindex()

import socket
iface_name = socket.if_nameindex()[0][1]
idx = socket.if_nametoindex(iface_name)

import socket
iface_idx = socket.if_nameindex()[0][0]
name = socket.if_indextoname(iface_idx)

import socket, threading
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]
def _client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", port))
    c.close()
t = threading.Thread(target=_client)
t.start()
conn, addr = srv.accept()
conn.close()
t.join()
srv.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 0))
s.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.close()

import socket, threading
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]
t = threading.Thread(target=lambda: srv.accept()[0].close())
t.start()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))
c.close()
t.join()
srv.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = s.dup()
s2.close()
s.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
flag = s.get_inheritable()
s.close()

import socket, threading
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]
t = threading.Thread(target=lambda: srv.accept()[0].close())
t.start()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))
peer = c.getpeername()
c.close()
t.join()
srv.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 0))
addr = s.getsockname()
s.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
val_type = s.getsockopt(socket.SOL_SOCKET, socket.SO_TYPE)
val_nodelay = s.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)
s.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 0))
s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
s.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 0))
s.listen(5)
s.close()

import socket, threading
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]
def _server():
    conn, _ = srv.accept()
    conn.sendall(b"hello")
    conn.close()
t = threading.Thread(target=_server)
t.start()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))
data = c.recv(1024)
c.close()
t.join()
srv.close()

import socket, threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 0))
port = s.getsockname()[1]
def _sender():
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender.sendto(b"ping", ("127.0.0.1", port))
    sender.close()
t = threading.Thread(target=_sender)
t.start()
data, addr = s.recvfrom(1024)
t.join()
s.close()

import socket, threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 0))
port = s.getsockname()[1]
buf = bytearray(1024)
def _sender():
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender.sendto(b"ping", ("127.0.0.1", port))
    sender.close()
t = threading.Thread(target=_sender)
t.start()
nbytes, addr = s.recvfrom_into(buf)
t.join()
s.close()

import socket, threading
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]
buf = bytearray(1024)
def _server():
    conn, _ = srv.accept()
    conn.sendall(b"hello")
    conn.close()
t = threading.Thread(target=_server)
t.start()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))
nbytes = c.recv_into(buf)
c.close()
t.join()
srv.close()

import socket, threading
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]
t = threading.Thread(target=lambda: srv.accept()[0].close())
t.start()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))
c.send(b"hello")
c.close()
t.join()
srv.close()

import socket, threading
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]
t = threading.Thread(target=lambda: srv.accept()[0].close())
t.start()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))
c.sendall(b"hello world " * 100)
c.close()
t.join()
srv.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"ping", ("127.0.0.1", 9))
s.close()

import socket, threading, tempfile, os
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]
t = threading.Thread(target=lambda: srv.accept()[0].close())
t.start()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))
with tempfile.NamedTemporaryFile(delete=False) as f:
    f.write(b"x" * 4096)
    fname = f.name
with open(fname, "rb") as f:
    c.sendfile(f)
c.close()
t.join()
srv.close()
os.unlink(fname)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.set_inheritable(True)
s.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(False)
s.setblocking(True)
s.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5.0)
s.settimeout(3.0)
s.settimeout(None)
s.close()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.close()

import socket, threading
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(("127.0.0.1", 0))
srv.listen(1)
port = srv.getsockname()[1]
t = threading.Thread(target=lambda: srv.accept()[0].close())
t.start()
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", port))
c.shutdown(socket.SHUT_RDWR)
c.close()
t.join()
srv.close()

import socket, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
info_bytes = s.share(os.getpid())
s.close()
