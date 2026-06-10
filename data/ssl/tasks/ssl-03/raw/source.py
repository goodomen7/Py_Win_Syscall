import ssl
import sys
import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- ssl.get_server_certificate ---
host = "www.python.org"
port = 443
_xperf_mark("BEGIN")
cert = ssl.get_server_certificate((host, port))
_xperf_mark("END")
