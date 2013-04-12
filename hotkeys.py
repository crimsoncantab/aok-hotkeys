#!/bin/python3
import sys

hotkeys = {
	'ground' : (0xB4, 'Attack Ground'),
	'convert' : (0x84, 'Convert'),
	'delete' : (0x9C, 'Delete Unit'),
	'build' : (0xC, 'Economic Buildings'),
	'garrison' : (0x90, 'Garrison'),
	'heal' : (0x78, 'Heal'),
	'mbuild' : (0x18, 'Military Buildings'),
	'pack' : (0x60, 'Pack'),
	'repair' : (0x24, 'Repair'),
	'setgather' : (0xA8, 'Set Gather Point'),
	'stop' : (0x48, 'Stop'),
	'unload' : (0x54, 'Unload'),
	'unpack' : (0x6C, 'Unpack'),
	
	'chatmenu' : (0x394, 'Chat Dialog'),
	'diplomacy' : (0x370, 'Diplomacy'),
	'time' : (0x2E0, 'Display Game Time'),
	'stats' : (0x250, 'Display Statistics'),
	'tech' : (0x2C8, 'Display Technology Tree'),
	'flare' : (0x304, 'Flare'),
	'range' : (0x268, 'Go to Archery Range'),
	'rax' : (0x25C, 'Go to Barracks'),
	'smith' : (0x2A4, 'Go to Blacksmith'),
	'castle' : (0x310, 'Go to Castle'),
	'dock' : (0x28C, 'Go to Dock'),
	'last' : (0x1F0, 'Go to Last Notification'),
	'last2' : (0x1FC, 'Go to Last Notification (2)'),
	'lumber' : (0x328, 'Go to Lumber Camp'),
	'market' : (0x22C, 'Go to Market'),
	'mill' : (0x2B0, 'Go to Mill'),
	'mining' : (0x31C, 'Go to Mining Camp'),
	'monastery' : (0x298, 'Go to Monastery'), #R
	'idlem' : (0x2EC, 'Go to Next Idle Military Unit'),#S
	'idlem2' : (0x2F8, 'Go to Next Idle Military Unit (2)'),#T
	'idlev' : (0x1D8, 'Go to Next Idle Villager'),#U
	'idlev2' : (0x1E4, 'Go to Next Idle Villager (2)'),#V
	'selected' : (0x208, 'Go to Selected Object'),#W
	'siege' : (0x280, 'Go to Siege Workshop'),#X
	'stable' : (0x274, 'Go to Stable'),
	'tc' : (0x214, 'Go to Town Center'),#Z
	'tc2' : (0x220, 'Go to Town Center (2)'),#SA
	'university' : (0x2BC, 'Go to University'),
	'cmap' : (0x334, 'Mini-map Combat Mode'),
	'emap' : (0x340, 'Mini-map Economic Mode'),#SD
	'nmap' : (0x34C, 'Mini-map Normal Mode'),
	'object': (0x388, 'Objectives'),
	'pause' : (0x3A0, 'Pause Game'),#SG
	'back' : (0x3C4, 'Return to Previous View'),
	'chatback' : (0x238, 'Review Chat Messages Backward'),
	'chatfor' : (0x244, 'Review Chat Messages Forward'),
	'chapter' : (0x3D0, 'Save Chapter'),#SK
	'save' : (0x3AC, 'Save Game'),
	'chat' : (0x1B4, 'Send Chat Message'),
	'slow' : (0x1CC, 'Slow Down Game'),
	'fast' : (0x1C0, 'Speed Up Game'),#SO
	'colors' : (0x3B8, 'Toggle Friend or Foe Colors'),
	
	'down' : (0x404, 'Scroll Down'),
	'left' : (0x3E0, 'Scroll Left'),
	'right' : (0x3EC, 'Scroll Right'),
	'up' : (0x3F8, 'Scroll Up'),#ST
	
	'brange' : (0x540, 'Archery Range'),
	'brax' : (0x4D4, 'Barracks'),
	'bsmith' : (0x4BC, 'Blacksmith'),
	'bbombard' : (0x510, 'Bombard Tower'),
	'bcastle' : (0x594, 'Castle'),
	'bdock' : (0x4C8, 'Dock'),#SZ
	'bfarm' : (0x534, 'Farm'),#CA
	'btrap' : (0x5D0, 'Fish Trap'),
	'bgate' : (0x51C, 'Gate'),
	'bhouse' : (0x4A4, 'House'),
	'blumber' : (0x5B8, 'Lumber Camp'),
	'bmarket' : (0x4EC, 'Market'),
	'bmill' : (0x4B0, 'Mill'),
	'bmining' : (0x5C4, 'Mining Camp'),
	'bmonastery' : (0x558, 'Monastery'),
	'bnext' : (0x5E8, 'More Buildings'),
	'boutpost' : (0x5DC, 'Outpost'),
	'bpalisade' : (0x4E0, 'Palisade Wall'),
	'bsiege' : (0x570, 'Siege Workshop'),
	'bstable' : (0x54C, 'Stable'),
	'bwall' : (0x4F8, 'Stone Wall'),
	'btower' : (0x504, 'Tower'),
	'btc' : (0x564, 'Town Center'),#CQ
	'buniversity' : (0x57C, 'University'),
	'bwonder' : (0x588, 'Wonder'),
	
	'work' : (0x64C, 'Go Back to Work'),
	'bell' : (0x640, 'Ring Town Bell'),
	'vill' : (0x5F8, 'Villager'),#CV
	
	#dock.  can we have conflict with different pages?  hotkey to go to next page?
	'longboat' : (0x6BC, 'Build Longboat'),
	'gcannon' : (0x680, 'Cannon Galleon'),
	'demoship' : (0x698, 'Demolition Ship, Heavy Demolition Ship'),
	'fireship' : (0x68C, 'Fire Ship, Fast Fire Ship'),#CZ
	'fish' : (0x65C, 'Fishing Ship'),
	'galley' : (0x674, 'Galley, War Galley, Galleon'),
	'cog' : (0x668, 'Trade Cog'),
	'transport' : (0x6B0, 'Transport'),
	'turtle' : (0x6C8, 'Turtle Ship, Elite Turtle Ship'),
	
	'eagle' : (0x6F0, 'Eagle Warrior, Elite Eagle Warrior'),#AF
	'huskarl' : (0x6FC, 'Huskarl'),
	'sword' : (0x6D8, 'Milita, Man-at-Arms, etc. (swordsmen)'),
	'spear' : (0x6E4, 'Spearman, Pikeman, Halberdier'),
	
	'archer' : (0x70C, 'Archer, Crossbowman, Arbalest (archers)'),
	'cavarcher' : (0x724, 'Cavarly Archer, Heavy Cavalry Archer'),
	'hcannon' : (0x730, 'Hand Cannoneer'),
	'skirm' : (0x718, 'Skirmister, Elite Skirmisher'),
	
	'camel' : (0x74C, 'Camel, Heavy Camel'),
	'knight' : (0x758, 'Knit, Cavalier, Paladin (knights)'),#AO
	'scout' : (0x740, 'Scout Cavalry, Light Cavalry, Hussar'),
	
	'ram' : (0x768, 'Battering Ram, Capped Ram, Siege Ram'),
	'bcannon' : (0x78C, 'Bombard Cannon'),
	'mangonel' : (0x780, 'Mangonel, Onager, Siege Onager'),
	'scorpion' : (0x774, 'Scorpion, Heavy Scorpion'),
	
	'mission' : (0x7A8, 'Missionary'),
	'monk' : (0x79C, 'Monk'),
	
	'cart' : (0x7B8, 'Trade Cart'),

	'agg' : (0x828, 'Aggressive'),
	'box' : (0x7D4, 'Box'),
	'def' : (0x834, 'Defensive'),#AZ
	'flank' : (0x7F8, 'Flank'),
	'follow' : (0x81C, 'Follow'),
	'guard' : (0x810, 'Guard'),
	'line' : (0x7E0, 'Line'),
	'noattack' : (0x84C, 'No Attack'),
	'patrol' : (0x804, 'Patrol'),
	'stag' : (0x7EC, 'Staggered'),
	'stand' : (0x840, 'Stand Ground'),
	
	'treb' : (0x85C, 'Build Trebuchet'),
	'uu' : (0x868, 'Build Unique Unit'),
	'petard' : (0x874, 'Petard'),

	'seed' : (0x884, 'Reseed Farm')
	}
