import msvcrt

result = msvcrt.kbhit()
key = msvcrt.getch()
test_char = b'A'
msvcrt.putch(test_char)