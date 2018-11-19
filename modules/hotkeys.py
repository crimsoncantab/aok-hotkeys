#!/usr/bin/python
import hkizip, struct
from collections import namedtuple
#these are derived from the numerical ids/text ids in the game configs
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
    'last2' : 0x1004a50,
    'lumber' : 0x4b5c,
    'market' : 0x4a53,
    'mill' : 0x4b4c,
    'mining' : 0x4b5b,
    'monastery' : 0x4b4a,
    'idlem' : 0x4a7c,
    'idlem2' : 0x1004a7c,
    'idlev' : 0x4a4f,
    'idlev2' : 0x1004a4f,
    'selected' : 0x4a51,
    'siege' : 0x4b48,
    'stable' : 0x4b47,
    'tc' : 0x4a52,
    'tc2' : 0x1004a52,
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
    'elephant' : 0x4a59,
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
    'seed' : 0x4a82,
    'cgroup0' : 0x2c32d,
    'cgroup1' : 0x4b2c,
    'cgroup2' : 0x4b2d,
    'cgroup3' : 0x4b2e,
    'cgroup4' : 0x4b2f,
    'cgroup5' : 0x4b30,
    'cgroup6' : 0x4b31,
    'cgroup7' : 0x4b32,
    'cgroup8' : 0x4b33,
    'cgroup9' : 0x4b34,
    'cgroup10' : 0x2c32e,
    'cgroup11' : 0x2c32f,
    'cgroup12' : 0x2c330,
    'cgroup13' : 0x2c331,
    'cgroup14' : 0x2c332,
    'cgroup15' : 0x2c333,
    'cgroup16' : 0x2c334,
    'cgroup17' : 0x2c335,
    'cgroup18' : 0x2c336,
    'cgroup19' : 0x2c337,
    'sgroup0' : 0x2c338,
    'sgroup1' : 0x4b36,
    'sgroup2' : 0x4b37,
    'sgroup3' : 0x4b38,
    'sgroup4' : 0x4b39,
    'sgroup5' : 0x4b3a,
    'sgroup6' : 0x4b3b,
    'sgroup7' : 0x4b3c,
    'sgroup8' : 0x4b3d,
    'sgroup9' : 0x4b3e,
    'sgroup10' : 0x2c339,
    'sgroup11' : 0x2c33a,
    'sgroup12' : 0x2c33b,
    'sgroup13' : 0x2c33c,
    'sgroup14' : 0x2c33d,
    'sgroup15' : 0x2c33e,
    'sgroup16' : 0x2c33f,
    'sgroup17' : 0x2c340,
    'sgroup18' : 0x2c341,
    'sgroup19' : 0x2c342,
    'attack' : 0x30d48,
    'bpgate' : 0x4b0c,
    'bfeitoria' : 0x4a83,
    'genitour' : 0x4a58,
    'siegetower' : 0x4a68,
    'caravel' : 0x4a6d,
}

valid_ids = set(hk_ids.values())

#the strings that (most) of the above numerical ids/text ids map to
hk_desc = {
    'ground' : 'Attack Ground',
    'convert' : 'Convert',
    'delete' : 'Delete Unit',
    'build' : 'Economic Buildings',
    'garrison' : 'Garrison',
    'heal' : 'Heal',
    'mbuild' : 'Military Buildings',
    'pack' : 'Pack',
    'repair' : 'Repair',
    'setgather' : 'Set Gather Point',
    'stop' : 'Stop',
    'unload' : 'Unload/Ungarrison',
    'unpack' : 'Unpack',
    'chatmenu' : 'Chat Dialog',
    'diplomacy' : 'Diplomacy',
    'time' : 'Display Game Time',
    'stats' : 'Display Statistics',
    'tech' : 'Display Technology Tree',
    'flare' : 'Flare',
    'range' : 'Go to Archery Range',
    'rax' : 'Go to Barracks',
    'smith' : 'Go to Blacksmith',
    'castle' : 'Go to Castle',
    'dock' : 'Go to Dock',
    'last' : 'Go to Last Notification',
    'last2' : 'Go to Last Notification (2)',
    'lumber' : 'Go to Lumber Camp',
    'market' : 'Go to Market',
    'mill' : 'Go to Mill',
    'mining' : 'Go to Mining Camp',
    'monastery' : 'Go to Monastery',
    'idlem' : 'Go to Next Idle Military Unit',
    'idlem2' : 'Go to Next Idle Military Unit (2)',
    'idlev' : 'Go to Next Idle Villager',
    'idlev2' : 'Go to Next Idle Villager (2)',
    'selected' : 'Go to Selected Object',
    'siege' : 'Go to Siege Workshop',
    'stable' : 'Go to Stable',
    'tc' : 'Go to Town Center',
    'tc2' : 'Go to Town Center (2)',
    'university' : 'Go to University',
    'cmap' : 'Mini-map Combat Mode',
    'emap' : 'Mini-map Economic Mode',
    'nmap' : 'Mini-map Normal Mode',
    'object' : 'Objectives',
    'pause' : 'Pause Game',
    'back' : 'Return to Previous View',
    'chatback' : 'Review Chat Messages Backward',
    'chatfor' : 'Review Chat Messages Forward',
    'chapter' : 'Save Chapter',
    'save' : 'Save Game',
    'chat' : 'Send Chat Message',
    'slow' : 'Slow Down Game',
    'fast' : 'Speed Up Game',
    'colors' : 'Toggle Friend or Foe Colors',
    'down' : 'Scroll Down',
    'left' : 'Scroll Left',
    'right' : 'Scroll Right',
    'up' : 'Scroll Up',
    'brange' : 'Archery Range',
    'brax' : 'Barracks',
    'bsmith' : 'Blacksmith',
    'bbombard' : 'Bombard Tower',
    'bcastle' : 'Castle',
    'bdock' : 'Dock',
    'bfarm' : 'Farm',
    'btrap' : 'Fish Trap',
    'bgate' : 'Gate',
    'bhouse' : 'House',
    'blumber' : 'Lumber Camp',
    'bmarket' : 'Market',
    'bmill' : 'Mill',
    'bmining' : 'Mining Camp',
    'bmonastery' : 'Monastery',
    'bnext' : 'More Buildings',
    'boutpost' : 'Outpost',
    'bpalisade' : 'Palisade Wall',
    'bpgate' : 'Palisade Gate',
    'bsiege' : 'Siege Workshop',
    'bstable' : 'Stable',
    'bwall' : 'Stone Wall',
    'btower' : 'Tower',
    'btc' : 'Town Center',
    'buniversity' : 'University',
    'bwonder' : 'Wonder',
    'bfeitoria' : 'Feitoria',
    'work' : 'Go Back to Work',
    'bell' : 'Ring Town Bell',
    'vill' : 'Villager',
    'longboat' : 'Longboat',
    'gcannon' : 'Cannon Galleon',
    'demoship' : 'Demolition Ship, Heavy Demolition Ship',
    'fireship' : 'Fire Ship, Fast Fire Ship',
    'fish' : 'Fishing Ship',
    'galley' : 'Galley, War Galley, Galleon',
    'cog' : 'Trade Cog',
    'transport' : 'Transport',
    'caravel' : 'Longboat, Caravel',
    'turtle' : 'Turtle Ship, Elite Turtle Ship',
    'eagle' : 'Eagle Warrior, Elite Eagle Warrior',
    'huskarl' : 'Huskarl',
    'sword' : 'Milita, Man-at-Arms, etc. (swordsmen)',
    'spear' : 'Spearman, Pikeman, Halberdier',
    'archer' : 'Archer, Crossbowman, Arbalest (archers)',
    'cavarcher' : 'Cavarly Archer, Heavy Cavalry Archer',
    'genitour' : 'Genitour',
    'hcannon' : 'Hand Cannoneer, Slinger',
    'skirm' : 'Skirmister, Elite Skirmisher',
    'camel' : 'Camel, Heavy Camel',
    'knight' : 'Knight, Cavalier, Paladin (knights)',
    'scout' : 'Scout Cavalry, Light Cavalry, Hussar',
    'elephant' : 'Battle Elephant, Elite Battle Elephant',
    'ram' : 'Battering Ram, Capped Ram, Siege Ram',
    'bcannon' : 'Bombard Cannon',
    'mangonel' : 'Mangonel, Onager, Siege Onager',
    'scorpion' : 'Scorpion, Heavy Scorpion',
    'siegetower' : 'Siege Tower',
    'mission' : 'Missionary',
    'monk' : 'Monk',
    'cart' : 'Trade Cart',
    'attack' : 'Attack Move',
    'agg' : 'Aggressive',
    'box' : 'Box',
    'def' : 'Defensive',
    'flank' : 'Flank',
    'follow' : 'Follow',
    'guard' : 'Guard',
    'line' : 'Line',
    'noattack' : 'No Attack',
    'patrol' : 'Patrol',
    'stag' : 'Staggered',
    'stand' : 'Stand Ground',
    'treb' : 'Build Trebuchet',
    'uu' : 'Build Unique Unit',
    'petard' : 'Petard',
    'seed' : 'Reseed Farm',
    'cgroup0' : 'Create Group #0',
    'cgroup1' : 'Create Group #1',
    'cgroup2' : 'Create Group #2',
    'cgroup3' : 'Create Group #3',
    'cgroup4' : 'Create Group #4',
    'cgroup5' : 'Create Group #5',
    'cgroup6' : 'Create Group #6',
    'cgroup7' : 'Create Group #7',
    'cgroup8' : 'Create Group #8',
    'cgroup9' : 'Create Group #9',
    'cgroup10' : 'Create Group #10',
    'cgroup11' : 'Create Group #11',
    'cgroup12' : 'Create Group #12',
    'cgroup13' : 'Create Group #13',
    'cgroup14' : 'Create Group #14',
    'cgroup15' : 'Create Group #15',
    'cgroup16' : 'Create Group #16',
    'cgroup17' : 'Create Group #17',
    'cgroup18' : 'Create Group #18',
    'cgroup19' : 'Create Group #19',
    'sgroup0' : 'Select Group #0',
    'sgroup1' : 'Select Group #1',
    'sgroup2' : 'Select Group #2',
    'sgroup3' : 'Select Group #3',
    'sgroup4' : 'Select Group #4',
    'sgroup5' : 'Select Group #5',
    'sgroup6' : 'Select Group #6',
    'sgroup7' : 'Select Group #7',
    'sgroup8' : 'Select Group #8',
    'sgroup9' : 'Select Group #9',
    'sgroup10' : 'Select Group #10',
    'sgroup11' : 'Select Group #11',
    'sgroup12' : 'Select Group #12',
    'sgroup13' : 'Select Group #13',
    'sgroup14' : 'Select Group #14',
    'sgroup15' : 'Select Group #15',
    'sgroup16' : 'Select Group #16',
    'sgroup17' : 'Select Group #17',
    'sgroup18' : 'Select Group #18',
    'sgroup19' : 'Select Group #19'
}



hk_groups = [
	
	
	('Menus', [
        'object',
        'tech' ,
        'chatmenu' ,
        'diplomacy'
	]),
	('Settings', [
        'colors',
        'stats' ,
        'time' ,
        'emap' ,
        'cmap' ,
        'nmap' ,
        'slow' ,
        'fast'
	]),
	('Game Commands', [
        'flare' ,
        'pause' ,
        'save' ,
        'chapter'
	]),
	('Chat', [
        'chat' ,
        'chatback' ,
        'chatfor' ,
	]),
	('Scrolling', [
        'up',
        'left' ,
        'right' ,
        'down'
	]),
	('Control Groups', [
        'cgroup0',
        'cgroup1',
        'cgroup2',
        'cgroup3',
        'cgroup4',
        'cgroup5',
        'cgroup6',
        'cgroup7',
        'cgroup8',
        'cgroup9',
        'cgroup10',
        'cgroup11',
        'cgroup12',
        'cgroup13',
        'cgroup14',
        'cgroup15',
        'cgroup16',
        'cgroup17',
        'cgroup18',
        'cgroup19',
        'sgroup0',
        'sgroup1',
        'sgroup2',
        'sgroup3',
        'sgroup4',
        'sgroup5',
        'sgroup6',
        'sgroup7',
        'sgroup8',
        'sgroup9',
        'sgroup10',
        'sgroup11',
        'sgroup12',
        'sgroup13',
        'sgroup14',
        'sgroup15',
        'sgroup16',
        'sgroup17',
        'sgroup18',
        'sgroup19'
	]),
	('Go-To Commands', [
        'mill' ,
        'mining' ,
        'lumber' ,
        'dock' ,
        'smith' ,
        'market' ,
        'monastery' ,
        'university' ,
        'tc' ,
        'tc2' ,
        'rax' ,
        'range' ,
        'stable' ,
        'siege' ,
        'castle' ,
        'idlem' ,
        'idlem2' ,
        'idlev' ,
        'idlev2' ,
        'selected' ,
        'last' ,
        'last2' ,
        'back'
	]),
	('All Units', [
        'delete' ,
        'garrison' ,
        'stop'
	]),
	('Military Units', [
        'attack' ,
        'patrol' ,
        'guard' ,
        'follow' ,
        'agg' ,
        'def' ,
        'stand',
        'noattack' ,
        'line' ,
        'box' ,
        'stag' ,
        'flank'
	]),
	('Siege Units', [
        'unpack',
        'pack' ,
        'ground' #onager is different spot
	]),
	('Monks', [
        'convert' ,
        'heal'
	]),
	('Villagers', [
        'build' ,
        'mbuild' ,
        'repair'
	]),
	('Buildings/Transports', [
        'setgather' ,
        'work',
        'unload' #transport is different spot
	]),('Economic Build Menu', [
        'bhouse' ,
        'bmill' ,
        'bmining' ,
        'blumber' ,
        'bdock' ,
        'bfarm' ,
        'bsmith' ,
        'bmarket' ,
        'bmonastery' ,
        'buniversity' ,
        'btc' ,
        'bwonder',
        'bfeitoria',
        'bnext'
	]),('Military Build Menu', [
        'brax' ,
        'brange' ,
        'bstable' ,
        'bsiege' ,
        'boutpost' ,
        'bpalisade' ,
        'bwall' ,
        'btower' ,
        'bbombard' ,
        'bgate' ,
        'bpgate' ,
        'bcastle'
	]),
	('Fishing Ship Build', [
        'btrap'
	]),
	('Town Center', [
        'vill',
        'bell'
	]),
	('Dock', [
        'fish' ,
        'transport' ,
        'cog' ,
        'galley' ,
        'demoship' ,
        'fireship' ,
        'gcannon' ,
        'longboat' ,
        'caravel' ,
        'turtle'
	]),
	('Barracks', [
        'sword' ,
        'spear' ,
        'huskarl' ,
        'eagle'
	]),
	('Archery Range', [
        'archer' ,
        'skirm' ,
        'cavarcher' ,
        'genitour' ,
        'hcannon'
	]),
	('Stable', [
        'scout',
        'knight' ,
        'camel',
        'elephant',
	]),
	('Siege Workshop', [
        'ram' ,
        'mangonel' ,
        'scorpion',
        'bcannon',
        'siegetower'
	]),
	('Monastery', [
        'monk',
        'mission'
	]),
	('Market', [
        'cart'
	]),
	('Castle', [
        'uu' ,
        'treb' ,
        'petard'
	]),
	('Mill', [
        'seed'
	])
]

hk_versions = [
    ('aok', 0x3f800000, 2080, 'Vanilla AoK'),
    ('aoc', 0x3f800000, 2192, 'AoC/FE/HD2.0'),
    ('22' , 0x40000000, 2432, 'HD2.2-3'),
    ('24' , 0x40400000, 2192, 'HD2.4-8'),
    ('30' , 0x40400000, 2204, 'HD3.0-4.3'),
    ('44' , 0x40400000, 2252, 'HD4.4-4.9'),
    ('50' , 0x40400000, 2264, 'HD5.0+'),
]
header_format = count_format = struct.Struct('<I')
hk_format = struct.Struct('<Ii???x')
Hotkey = namedtuple('Hotkey', 'code id ctrl alt shift')

def copy_dict(d, *keys):
    return {key: d[key] for key in keys}

class HotkeyAssign:
    def __init__(self, hkfile):
        self.version, self.hotkeys = hkfile.version, { k : copy_dict(v,'code', 'ctrl', 'alt', 'shift') for (k,v) in hkfile}
        self.update()
        
    def get_hotkeys(self, version_hotkeys):
        return {k : v for (k,v) in self.hotkeys.items() if k in version_hotkeys}

    def update(self):
        self.hotkeys.update({ k : {'code':0, 'ctrl' : False, 'alt' : False, 'shift' : False} for k in hk_desc if k not in self.hotkeys})


class HotkeyFile:

    def __init__(self, hki):
        hk_data = hkizip.decompress(hki)
        offset = 0
        header, = header_format.unpack_from(hk_data, offset)
        version = None
        for (k, head, size, desc) in hk_versions:
            if len(hk_data) == size and header == head:
                version = k
        if not version:
            raise Exception('Unrecognized file format, header: {:x}, length: {:d}'.format(header, len(hk_data)))
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
                hotkey = Hotkey(*hk_format.unpack_from(hk_data, offset))._asdict()
                id = hotkey['id']
                if (id != -1):
                    while id in hk_map: id+=0x1000000
                    hk_map[id] = hotkey
                    if id not in valid_ids:
                        raise Exception('Corrupted file: {:x}'.format(id))
                offset += hk_format.size
                menu.append(hotkey)

        
        self.data, self.hk_map, self.version = data, hk_map, version
        self._header, self._file_size= header, offset

    def __getitem__(self, key):
        return self.hk_map[hk_ids[key]]

    def __contains__(self, key):
        return key in hk_ids and hk_ids[key] in self.hk_map
        
    def __iter__(self):
        for k in hk_ids:
            if k in self:
                yield k, self[k]

    def serialize(self):
        offset = 0
        #update raw from data
        raw = bytearray(self._file_size)
        header_format.pack_into(raw, offset, self._header)
        offset += header_format.size
        count_format.pack_into(raw, offset, len(self.data))
        offset += count_format.size
        for menu in self.data:
            count_format.pack_into(raw, offset, len(menu))
            offset += count_format.size
            for hotkey in menu:
                hk_format.pack_into(raw, offset, *Hotkey(**hotkey))
                offset += hk_format.size
        assert offset == self._file_size
        return hkizip.compress(str(raw))

if __name__ == '__main__':
	import sys
	hki = sys.stdin.read()
	hotkey_file = HotkeyFile(hki)
	for i, hk in enumerate(hk_groups[2][1]):
		hotkey_file[hk]['code'] = 252 - i
    
	#print hotkey_file.data
