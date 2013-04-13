#!/bin/python3
import sys
import zlib

def compress(input):
    c = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -zlib.MAX_WBITS, zlib.DEF_MEM_LEVEL, zlib.Z_DEFAULT_STRATEGY)
    output = c.compress(input)
    return output + c.flush()

def decompress(input):
    d = zlib.decompressobj(-zlib.MAX_WBITS)
    output = d.decompress(input)
    return output + d.flush()

if __name__ == '__main__':
    stdinb = sys.stdin.buffer
    stdoutb = sys.stdout.buffer
    f = decompress if sys.argv[1] == 'd' else compress
    stdoutb.write(f(stdinb.read()))
