#!/bin/python3
import hotkeys
import string
import sys

stdinb = sys.stdin.buffer
stdoutb = sys.stdout.buffer

hkbytes = bytearray(stdinb.read())
zeros = bytearray([0])*3
print(hex(len(hkbytes)), file=sys.stderr)
for hk, val in zip(hklist, (string.ascii_uppercase*5)[:-1]):
	loc = hotkeys[hk][0]
	
	hkbytes[loc] = ord(val)
	hkbytes[loc+8:loc+11] = zeros
	

stdoutb.write(hkbytes)


