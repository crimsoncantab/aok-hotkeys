#!/bin/python
import hkizip, struct

hk_ids = {
'ground' : 0x4b14,
'convert' : 0x4b16,
'delete' : 0x4a38,
'build' : 0x4b0e,
'garrison' : 0x4a44,
'heal' : 0x4b15,
'mbuild' : 0x4b0f,
'pack' : 0x4b29,
'repair' : 0x4b18,
'setgather' : 0x4a3a,
'stop' : 0x4b10,
'unload' : 0x4b19,
'unpack' : 0x4b2a,
'chatmenu' : 0x4b65,
'diplomacy' : 0x4b62,
'time' : 0x4a42,
'stats' : 0x4b44,
'tech' : 0x4b52,
'flare' : 0x4b59,
'range' : 0x4b46,
'rax' : 0x4b45,
'smith' : 0x4b4b,
'castle' : 0x4b5a,
'dock' : 0x4b49,
'last' : 0x4a50,
'last2' : 0x14a50,
'lumber' : 0x4b5c,
'market' : 0x4a53,
'mill' : 0x4b4c,
'mining' : 0x4b5b,
'monastery' : 0x4b4a,
'idlem' : 0x4a7c,
'idlem2' : 0x14a7c,
'idlev' : 0x4a4f,
'idlev2' : 0x14a4f,
'selected' : 0x4a51,
'siege' : 0x4b48,
'stable' : 0x4b47,
'tc' : 0x4a52,
'tc2' : 0x14a52,
'university' : 0x4b4d,
'cmap' : 0x4b5d,
'emap' : 0x4b5e,
'nmap' : 0x4b5f,
'object' : 0x4b64,
'pause' : 0x4b7b,
'back' : 0x4b7e,
'chatback' : 0x4a54,
'chatfor' : 0x4a55,
'chapter' : 0x4b80,
'save' : 0x4b7d,
'chat' : 0x4a39,
'slow' : 0x4a3d,
'fast' : 0x4a3c,
'colors' : 0x4b7f,
'down' : 0x4a41,
'left' : 0x4a3e,
'right' : 0x4a3f,
'up' : 0x4a40,
'brange' : 0x4a76,
'brax' : 0x4a78,
'bsmith' : 0x4a77,
'bbombard' : 0x4b04,
'bcastle' : 0x4a7a,
'bdock' : 0x4a7b,
'bfarm' : 0x4b00,
'btrap' : 0x4b02,
'bgate' : 0x4b40,
'bhouse' : 0x4b0d,
'blumber' : 0x4b53,
'bmarket' : 0x4b25,
'bmill' : 0x4b24,
'bmining' : 0x4b58,
'bmonastery' : 0x4a79,
'bnext' : 0x4b2b,
'boutpost' : 0x4b03,
'bpalisade' : 0x4b0a,
'bsiege' : 0x4b05,
'bstable' : 0x4b06,
'bwall' : 0x4b0b,
'btower' : 0x4b01,
'btc' : 0x4b26,
'buniversity' : 0x4b08,
'bwonder' : 0x4b09,
'work' : 0x4b7c,
'bell' : 0x4b77,
'vill' : 0x4a6e,
'longboat' : 0x4b78,
'gcannon' : 0x4a6f,
'demoship' : 0x4b50,
'fireship' : 0x4b4f,
'fish' : 0x4a65,
'galley' : 0x4a73,
'cog' : 0x4a64,
'transport' : 0x4b54,
'turtle' : 0x4a80,
'eagle' : 0x4a7e,
'huskarl' : 0x4a81,
'sword' : 0x4a5b,
'spear' : 0x4a5a,
'archer' : 0x4a5e,
'cavarcher' : 0x4a60,
'hcannon' : 0x4a61,
'skirm' : 0x4a63,
'camel' : 0x4a57,
'knight' : 0x4a56,
'scout' : 0x4a74,
'ram' : 0x4a70,
'bcannon' : 0x4a67,
'mangonel' : 0x4b55,
'scorpion' : 0x4a69,
'mission' : 0x4a7f,
'monk' : 0x4a6b,
'cart' : 0x4b56,
'agg' : 0x4b73,
'box' : 0x4b67,
'def' : 0x4b74,
'flank' : 0x4b6a,
'follow' : 0x4b72,
'guard' : 0x4b71,
'line' : 0x4b68,
'noattack' : 0x4b76,
'patrol' : 0x4b70,
'stag' : 0x4b69,
'stand' : 0x4b75,
'treb' : 0x4b79,
'uu' : 0x4b7a,
'petard' : 0x4a7d,
'seed' : 0x4a82
}


hk_loc = {
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

hk_order = [
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

class HotkeyFile:

    def __init__(self, hki):
        header_format = count_format = struct.Struct('<I')
        hk_format = struct.Struct('<II???x')
        hk_data = hkizip.decompress(hki)
        offset = 0
        header, = header_format.unpack_from(hk_data, offset)
        offset += header_format.size
        num_menus, = count_format.unpack_from(hk_data, offset)
        offset += count_format.size
        data = []
        hk_map = {}
        for i in range(num_menus):
            menu = []
            data.append(menu)
            menu_size, = count_format.unpack_from(hk_data, offset)
            offset += count_format.size
            for j in range(menu_size):
                hotkey, id, ctrl, alt, shift = hk_format.unpack_from(hk_data, offset)
                if (id != 0xffffffff):
                    while id in hk_map: id+=0x10000
                    hk_map[id] = (i,j)
                offset += hk_format.size
                menu.append((hotkey, id, ctrl, alt, shift))

        self.header_format, self.count_format, self.hk_format = header_format, count_format, hk_format
        self.header, self.data, self.hk_map = header, data, hk_map



def set_hotkeys(inbytes, **assign):
    #infile should be uncompressed
    for hk in hk_order:
        pos, desc = hk_loc[hk]
        if hk in assign:
            a = assign[hk]
        else:
            a = (0, 0, 0, 0)
        inbytes[pos] = a[0]
        inbytes[pos+8:pos+11] = a[1:4]

if __name__ == '__main__':
    import sys
    hki = sys.stdin.read()
    hotkey_file = HotkeyFile(hki)
    hku = bytearray(hkizip.decompress(hki))
    print len(hotkey_file.hk_map), sum([len(menu) for menu in hotkey_file.data])
    # for hk in hk_order:
        # pos = hk_loc[hk][0]
        # id = hku[pos+4] + (hku[pos+5]<<8)
        # print '\'{:s}\' : 0x{:x},'.format(hk, id)
