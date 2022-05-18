import re
import hotkeys
import ConfigParser as configparser
import hkstrings

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


def print_for_key(char='A'):
    ds = [d for l in hkfile.data for d in l if
          (d['code'] in {ord(char), ord(char) + 32} and not d['ctrl'] and not d['shift'] and not d['alt'])]
    ids = {d['id'] for d in ds}
    for (k, v) in hkstrings.hk_mapping.items():
        if v[0] in ids: print (k, v)


def main():
    global hkfile
    with open(sys.argv[1]) as stringsfile:
        string_map = get_string_mapping(stringsfile)
    with open(sys.argv[2], 'rb') as hkifile:
        hki = hkifile.read()
    hkfile = hotkeys.HotkeyFile(hki, False)
    print(hkfile._file_size)
    print(hkfile.orphan_ids)
    descs = {i: string_map.get(i, 'UNKNOWN') for i in hkfile.orphan_ids}
    for k, v in descs.items():
        print('\'\' : (0x{:x}, {}),'.format(k, repr(v)))

if __name__ == '__main__':
    import sys

    main()
