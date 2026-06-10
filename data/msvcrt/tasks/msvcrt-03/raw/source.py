# putch_xperf.py
import msvcrt
import sys
import os

def _xperf_mark(name):
    try:
        open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError:
        pass

test_char = b'A'  # Character to output

_xperf_mark("BEGIN")
msvcrt.putch(test_char)  # Output a character to the console
_xperf_mark("END")
