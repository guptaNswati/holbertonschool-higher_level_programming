#!/usr/bin/python3
letter = ""
for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    else:
        letter += chr(i)
print(letter, end="")
