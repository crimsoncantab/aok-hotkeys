#!/bin/python
import sys
import zlib
import itertools

def compress(input):
    c = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -zlib.MAX_WBITS, zlib.DEF_MEM_LEVEL, zlib.Z_DEFAULT_STRATEGY)
    output = c.compress(input)
    return output + c.flush()
    # comp, wbit, mem = 6, 12, 3
    # c = zlib.compressobj(comp, zlib.DEFLATED, -wbit, mem, zlib.Z_DEFAULT_STRATEGY)
    # for comp, wbit, mem, strat in itertools.product(range(-1, 10), range(8, 16), range(1,10), range(0,5)):
        # c = zlib.compressobj(comp, zlib.DEFLATED, -wbit, mem, strat)
        # output = c.compress(input) + c.flush()
        # if len(output) == 597:
            # with open('a%d_%d_%d_%d.hki' % (comp, wbit, mem, strat), 'wb') as out:
                # out.write(output)

def decompress(input):
    d = zlib.decompressobj(-zlib.MAX_WBITS)
    output = d.decompress(input)
    return output + d.flush()

if __name__ == '__main__':
    try:
        stdinb = sys.stdin.buffer
        stdoutb = sys.stdout.buffer
    except:
        stdinb = sys.stdin
        stdoutb = sys.stdout
    f = decompress if sys.argv[1] == 'd' else compress
    stdoutb.write(f(stdinb.read()))
    # compress(sys.stdin.read())
