#!/bin/python3
from hotkeys import hotkeys
import string
import sys

hklist = [
	'ground' ,
	'convert' ,
	'delete' ,
	'build' ,
	'garrison' ,
	'heal' ,
	'mbuild' ,
	'pack' ,
	'repair' ,
	'setgather' ,
	'stop' ,
	'unload' ,
	'unpack' ,
	
	'chatmenu' ,
	'diplomacy' ,
	'time' ,
	'stats' ,
	'tech' ,
	'flare' ,
	'range' ,
	'rax' ,
	'smith' ,
	'castle' ,
	'dock' ,
	'last' ,
	'last2' ,
	'lumber' ,
	'market' ,
	'mill' ,
	'mining' ,
	'monastery' , #R
	'idlem' ,#S
	'idlem2' ,#T
	'idlev' ,#U
	'idlev2' ,#V
	'selected' ,#W
	'siege' ,#X
	'stable' ,
	'tc' ,#Z
	'tc2' ,#SA
	'university' ,
	'cmap' ,
	'emap' ,#SD
	'nmap' ,
	'object',
	'pause' ,#SG
	'back' ,
	'chatback' ,
	'chatfor' ,
	'chapter' ,#SK
	'save' ,
	'chat' ,
	'slow' ,
	'fast' ,#SO
	'colors' ,
	
	'down' ,
	'left' ,
	'right' ,
	'up' ,#ST
	
	'brange' ,
	'brax' ,
	'bsmith' ,
	'bbombard' ,
	'bcastle' ,
	'bdock' ,#SZ
	'bfarm' ,#CA
	'btrap' ,
	'bgate' ,
	'bhouse' ,
	'blumber' ,
	'bmarket' ,
	'bmill' ,
	'bmining' ,
	'bmonastery' ,
	'bnext' ,
	'boutpost' ,
	'bpalisade' ,
	'bsiege' ,
	'bstable' ,
	'bwall' ,
	'btower' ,
	'btc' ,#CQ
	'buniversity' ,
	'bwonder' ,
	
	'work' ,
	'bell' ,
	'vill' ,#CV
	
	#dock.  can we have conflict with different pages?  hotkey to go to next page?
	'longboat' ,
	'gcannon' ,
	'demoship' ,
	'fireship' ,#CZ
	'fish' ,
	'galley' ,
	'cog' ,
	'transport' ,
	'turtle' ,
	
	'eagle' ,#AF
	'huskarl' ,
	'sword' ,
	'spear' ,
	
	'archer' ,
	'cavarcher' ,
	'hcannon' ,
	'skirm' ,
	
	'camel' ,
	'knight' ,#AO
	'scout' ,
	
	'ram' ,
	'bcannon' ,
	'mangonel' ,
	'scorpion' ,
	
	'mission' ,
	'monk' ,
	
	'cart' ,

	'agg' ,
	'box' ,
	'def' ,#AZ
	'flank' ,
	'follow' ,
	'guard' ,
	'line' ,
	'noattack' ,
	'patrol' ,
	'stag' ,
	'stand' ,
	
	'treb' ,
	'uu' ,
	'petard' ,

	'seed'
	]

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


