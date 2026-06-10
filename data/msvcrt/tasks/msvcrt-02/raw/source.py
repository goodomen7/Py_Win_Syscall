# getch_xperf.py
import msvcrt
import sys
import os

def _xperf_mark(name):
    try: 
        open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: 
        pass

_xperf_mark("BEGIN")
key = msvcrt.getch()  # Wait for and get a single character
_xperf_mark("END")
