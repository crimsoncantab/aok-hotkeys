#!/usr/bin/python
import hkizip, hkparse, hkstrings

# these are derived from the numerical ids/text ids in the game configs
_hk_names = {k: v[0] for k, v in hkstrings.hk_mapping.items()}
# the reverse of _hk_names
_hk_ids = {v: k for k, v in _hk_names.iteritems()}
_valid_ids = set(_hk_ids.keys())
# the strings that the above numerical ids/text ids map to
hk_desc = {k: v[1] for k, v in hkstrings.hk_mapping.items()}

hk_groups = hkstrings.hk_groups

hk_versions = [
    ('aok', 0x3f800000, 2080, 'Vanilla AoK'),
    ('aoc', 0x3f800000, 2192, 'AoC/FE/HD2.0'),
    ('22', 0x40000000, 2432, 'HD2.2-3'),
    ('24', 0x40400000, 2192, 'HD2.4-8'),
    ('30', 0x40400000, 2204, 'HD3.0-4.3'),
    ('44', 0x40400000, 2252, 'HD4.4-4.9'),
    ('50', 0x40400000, 2264, 'HD5.0+'),
    ('wk', 0x3f800000, 2240, 'WololoKingdoms'),
    ('deo', 0x40400000, 4632, 'DE (old)'),
    ('de', 0x40400000, 4644, 'Definitive Edition'),
]


def copy_dict(d, *keys):
    return {key: d[key] for key in keys}


class HotkeyAssign:
    def __init__(self, hkfile):
        self.version, self.hotkeys = hkfile.version, {k: copy_dict(v, 'code', 'ctrl', 'alt', 'shift') for (k, v) in
                                                      hkfile}
        self.update()

    def get_hotkeys(self, version_hotkeys):
        return {k: v for (k, v) in self.hotkeys.items() if k in version_hotkeys}

    def update(self):
        self.hotkeys.update(
            {k: {'code': 0, 'ctrl': False, 'alt': False, 'shift': False} for k in hk_desc if k not in self.hotkeys})


class HotkeyFile:

    def __init__(self, hki, validate=True):
        hk_bytes = hkizip.decompress(hki)
        parser = hkparse.HkParser()
        hk_dict = parser.parse_to_dict(hk_bytes)
        self._header = hk_dict['header']
        self._file_size = hk_dict['size']
        self.version = self._find_version(self._file_size, self._header)
        self.data = hk_dict['menus']
        self.hk_map, self.orphan_ids = self._build_id_map(self.data)
        if validate:
            parser.validate_size()
            self.validate()

    def validate(self):
        if not self.version:
            raise Exception(
                'Unrecognized file format, header: {:x}, length: {:d}'.format(self._header, self._file_size))
        if self.orphan_ids:
            raise Exception(
                'Unrecognized hotkey ids: {}'.format(','.join('{:d}'.format(i) for i in self.orphan_ids)))

    @staticmethod
    def _build_id_map(menus):
        hk_map = {}
        for menu in menus:
            for hotkey in menu:
                id = hotkey['id']
                if id >= 0:
                    while id in hk_map: id += 0x1000000
                    hk_map[id] = hotkey
        return hk_map, set(hk_map.keys()) - _valid_ids

    @staticmethod
    def _find_version(file_size, header):
        version = None
        for (k, head, size, desc) in hk_versions:
            if file_size == size and header == head:
                version = k
        return version

    def __getitem__(self, key):
        return self.hk_map[_hk_names[key]]

    def __contains__(self, key):
        return key in _hk_names and _hk_names[key] in self.hk_map

    def __iter__(self):
        for k in _hk_names:
            if k in self:
                yield k, self[k]

    def serialize(self):
        unparser = hkparse.HkUnparser()
        hk_dict = dict(size=self._file_size, header=self._header, menus=self.data)
        raw = unparser.unparse_to_bytes(hk_dict)
        return hkizip.compress(str(raw))


def _print_in_hk_file_order(hotkey_file):
    groups = {name for menu in hk_groups for name in menu[1]}
    for i, menu in enumerate(hotkey_file.data):
        print(i)
        for hotkey in menu:
            if hotkey['id'] in _hk_ids:
                name = _hk_ids[hotkey['id']]
                if name not in groups:
                    print(repr(_hk_ids[hotkey['id']]) + ',')


def _convert_to_single_map():
    for k in sys.stdin:
        k = k.strip()
        print('{} : (0x{:x}, {}),'.format(repr(k), _hk_names[k], repr(hk_desc[k])))


if __name__ == '__main__':
    import sys

    hki = sys.stdin.read()
    hotkey_file = HotkeyFile(hki, False)
    hotkey_file.validate()
    _print_in_hk_file_order(hotkey_file)
    # base_code = 0x2c338
    # for i in range(11):
    #     group_no = i+10
    #     print("'sgroup{:d}' : (0x{:x}, 'Select Group #{:d}'),".format(group_no, base_code+i, group_no))
