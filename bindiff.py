#!/bin/python3
import sys

with open(sys.argv[1], 'rb') as f1, open(sys.argv[2], 'rb') as f2:
	for i, (a, b) in enumerate(zip(f1.read(), f2.read())):
		if a != b:
			print(hex(i), chr(a), chr(b))