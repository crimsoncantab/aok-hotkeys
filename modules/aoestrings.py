import re
import hotkeys
import ConfigParser as configparser

AOESTRINGS = r'key-value-strings-utf8.txt'
WOLOLOSTRINGS = r'language.ini'


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


def get_ini_string_mapping(stringsfile):
    config = configparser.RawConfigParser()
    config.readfp(stringsfile)
    return {int(x): y for (x, y) in config.items('Default')}


if __name__ == '__main__':
    import sys

    # with open(AOESTRINGS) as stringsfile:
    #     string_map = get_string_mapping(stringsfile)
    with open(WOLOLOSTRINGS) as stringsfile:
        string_map = get_ini_string_mapping(stringsfile)
    hki = sys.stdin.read()
    hkfile = hotkeys.HotkeyFile(hki, False)
    print(hkfile._file_size)
    print(hkfile.orphan_ids)
    descs = {i: string_map.get(i, 'UNKNOWN') for i in hkfile.orphan_ids}
    with open('output.out', 'w') as output:
        for k, v in descs.items():
            output.write('\'\' : (0x{:x}, {}),\n'.format(k, repr(v)))
    hkfile.validate()
