#!/usr/bin/python
import struct
from collections import namedtuple

header_format = count_format = struct.Struct('<I')
hk_format = struct.Struct('<Ii???x')
Hotkey = namedtuple('Hotkey', 'code id ctrl alt shift')


class HkParser(object):

    def __init__(self):
        self._reset()

    def _reset(self, hk_bytes=None):
        self._offset = 0
        self._result = {}
        self._hk_bytes = hk_bytes

    def _unpack(self, struct_format=count_format):
        data = struct_format.unpack_from(self._hk_bytes, self._offset)
        self._offset += struct_format.size
        return data

    def _parse_header(self):
        self._result['header'], = self._unpack(header_format)

    def _parse_menus(self):
        num_menus, = self._unpack()
        self._result['menus'] = [self._parse_menu() for _ in range(num_menus)]

    def _parse_menu(self):
        num_hotkeys, = self._unpack()
        return [self._parse_hotkey() for _ in range(num_hotkeys)]

    def _parse_hotkey(self):
        return Hotkey(*self._unpack(hk_format))._asdict()

    def parse_to_dict(self, hk_bytes):
        self._reset(hk_bytes)
        self._parse_header()
        self._parse_menus()
        self._result['size'] = self._offset
        return self._result


class HkUnparser(object):

    def __init__(self):
        self._reset()

    def _reset(self, hk_dict=None):
        self._offset = 0
        self._hk_dict = hk_dict
        self._result = bytearray(hk_dict['size']) if hk_dict else None

    def _pack(self, *data, **kwargs):
        struct_format = kwargs.get('struct_format', count_format)
        struct_format.pack_into(self._result, self._offset, *data)
        self._offset += struct_format.size

    def _unparse_header(self, header):
        self._pack(header, struct_format=header_format)

    def _unparse_menus(self, menus):
        self._pack(len(menus))
        for menu in menus:
            self._unparse_menu(menu)

    def _unparse_menu(self, menu):
        self._pack(len(menu))
        for hotkey in menu:
            self._unparse_hotkey(hotkey)

    def _unparse_hotkey(self, hotkey):
        self._pack(*Hotkey(**hotkey))

    def unparse_to_bytes(self, hk_dict):
        self._reset(hk_dict)
        self._unparse_header(hk_dict['header'])
        self._unparse_menus(hk_dict['menus'])
        return self._result


if __name__ == '__main__':
    import sys

    hk = sys.stdin.read()
    hotkeys = HkParser().parse_to_dict(hk)
    print(hotkeys)
    assert hk == HkUnparser().unparse_to_bytes(hotkeys)

