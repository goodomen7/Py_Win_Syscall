# kbhit_xperf.py
import msvcrt
import sys
import os

def _xperf_mark(name):
    try:
        open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError:
        pass

# --- msvcrt.kbhit ---


_xperf_mark("BEGIN")
result = msvcrt.kbhit()  # Check if a key has been pressed
_xperf_mark("END")
