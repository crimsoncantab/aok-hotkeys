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
def alpha():
    for hk, val in zip(hotkeys.hk_order, (string.ascii_uppercase*5)[:-1]):
        loc = hotkeys.hk_loc[hk][0]

        hkbytes[loc] = ord(val)
        hkbytes[loc+8:loc+11] = zeros


    stdoutb.write(hkbytes)

def ids():
    #firstbytes = set()
    #secondbytes = set()
    for hk in hotkeys.hk_order:
        loc = hotkeys.hk_loc[hk][0]
        #firstbytes.add(hkbytes[loc+4])
        #secondbytes.add(hkbytes[loc+5])
        print hkbytes[loc+4], hk, hkbytes[loc+5]

def unset():
    for hk in hotkeys.hk_order:
        loc = hotkeys.hk_loc[hk][0]
        hkbytes[loc] = 0
    stdoutb.write(hkbytes)


def symbol():
    for hk in hotkeys.hk_order:
        if hk == 'monastery':
            break
        loc, desc = hotkeys.hk_loc[hk]
        print hex(hkbytes[loc]), hkbytes[loc], desc

def unsettable():
    hkbytes[hotkeys.hk_loc['delete'][0]] = 183
    hkbytes[hotkeys.hk_loc['delete'][0]+8] = 1
    #hkbytes[hotkeys.hk_loc['stop'][0]] = 0x5b
    #hkbytes[hotkeys.hk_loc['diplomacy'][0]] = 0x5c
    #hkbytes[hotkeys.hk_loc['diplomacy'][0]+8] = 1
    #hkbytes[hotkeys.hk_loc['chatmenu'][0]] = 0x5d
    #hkbytes[hotkeys.hk_loc['garrison'][0]] = 49
    #hkbytes[hotkeys.hk_loc['garrison'][0]+10] = 1
    #hkbytes[hotkeys.hk_loc['build'][0]] = 49
    #hkbytes[hotkeys.hk_loc['build'][0]+8] = 1
    stdoutb.write(hkbytes)
#symbol()
unsettable()
