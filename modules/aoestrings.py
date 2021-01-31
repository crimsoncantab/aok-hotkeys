import re
import hotkeys

AOESTRINGS = r'key-value-strings-utf8.txt'


def get_string_mapping(stringsfile):
    pattern = re.compile(
        r'([^\s/]+)\s+\"(.*)\".*'
    )
    d = {}
    for row in stringsfile:
        match = pattern.match(row)
        if match:
            key = match.group(1)
            value = match.group(2)
            try:
                key = int(key)
            except ValueError:
                pass
            d[key] = value
    return d


if __name__ == '__main__':
    import sys

    with open(AOESTRINGS) as stringsfile:
        string_map = get_string_mapping(stringsfile)
    hki = sys.stdin.read()
    hkfile = hotkeys.HotkeyFile(hki, False)
    print(hkfile._file_size)
    print(hkfile.orphan_ids)
    descs = {i: string_map.get(i, 'UNKNOWN') for i in hkfile.orphan_ids}
    with open('output.out', 'w') as output:
        for k, v in descs.items():
            output.write('\'\' : (0x{:x}, {}),\n'.format(k, repr(v)))
    hkfile.validate()
