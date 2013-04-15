#!/bin/python
import hotkeys
import string
import sys

try:
    stdinb = sys.stdin.buffer
    stdoutb = sys.stdout.buffer
except:
    stdinb = sys.stdin
    stdoutb = sys.stdout

hkbytes = bytearray(stdinb.read())
zeros = bytearray([0])*3
#print(hex(len(hkbytes)), file=sys.stderr)
for hk, val in zip(hotkeys.hk_order, (string.ascii_uppercase*5)[:-1]):
	loc = hotkeys.hk_loc[hk][0]
	
	hkbytes[loc] = ord(val)
	hkbytes[loc+8:loc+11] = zeros
	

stdoutb.write(hkbytes)


