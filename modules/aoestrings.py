import re
import hotkeys
import ConfigParser as configparser
import hkstrings

AOESTRINGS = r'key-value-strings-utf8.txt'
WOLOLOSTRINGS = r'language.ini'

cp_map = {
    19281: 'GoToKrepost',
    19329: 'GoToDonjon',

    16674: 'BuildKrepost',
    16710: 'BuildDonjon',
    16728: 'BuildCaravanserai',

    19054: 'CreateVillager',

    19081: 'Loom',
    19082: 'TownWatch',
    19083: 'Wheelbarrow',
    19152: 'GotNextAge',

    19045: 'CreateFishingShip',
    19044: 'CreateTradeCog',
    19059: 'CreateGalley',
    19055: 'CreateCannonGalleon',
    19279: 'CreateFireGalley',
    19280: 'CreateDemolitionShip',
    19284: 'CreateTransport',
    19320: 'CreateLongboat',
    19072: 'CreateTurtleShip',
    16662: 'galleyUpgrade',
    16664: 'Gillnets',
    16666: 'CareeningDryDock',
    16669: 'FastFireShip',
    16672: 'heavyDemoUpgrade',
    16676: 'EliteUniqueShip',
    16678: 'Shipwright',
    16681: 'EliteCannonUpgrade',
    16724: 'CreateCaravel',
    16726: 'CreateThirisadai',

    19035: 'CreateMilitia',
    19034: 'CreatePikeman',
    19070: 'CreateEagleWarrior',
    16718: 'CreateHuskarl',
    16600: 'MilitiaUpgrades',
    16602: 'PikemanUpgrade',
    16604: 'EagleUpgrade',
    16606: 'Supplies',
    16608: 'Squires',
    16610: 'Arson',
    19073: 'Condottiero',

    19038: 'CreateArcher',
    19043: 'CreateSkirmisher',
    19040: 'CreateCavArcher',
    19041: 'CreateHandCannoneer',
    19032: 'CreateGenitour',
    16612: 'ArcherUpgrades',
    16614: 'SkirmisherUpgrades',
    16616: 'EliteCavalryArcher',
    16618: 'Thumbring',
    16620: 'ParthianTactics',
    16622: 'EliteGenitour',
    16716: 'CreateEleArcher',
    16720: 'EliteEleArcher',

    19060: 'CreateScout',
    19031: 'CreateCamel',
    19030: 'CreateKnight',
    16712: 'CreateBattleElephant',
    5800: 'SteppeLancer',
    16624: 'ScoutUpgrades',
    16626: 'KnightUpgrades',
    16628: 'CamelUpgrades',
    16630: 'EliteSteppe',
    16632: 'Bloodlines',
    16634: 'Husbandry',
    16714: 'Tarkan',
    16722: 'EliteElephant',

    19056: 'CreateRam',
    19049: 'CreateScorpion',
    19285: 'CreateMangonel',
    19047: 'CreateBombardCannon',
    19048: 'CreateSiegeTower',
    16636: 'RamUpgrades',
    16638: 'OnagerUpgrades',
    16640: 'HeavyScorpion',
    16683: 'houfnice',

    19051: 'Monk',
    19071: 'Missionary',

    19116: 'Atonement',
    19117: 'BlockPrinting',
    19118: 'Faith',
    19119: 'Fervor',
    19120: 'HerbalMedicine',
    19121: 'Heresy',
    19122: 'Illumination',
    19123: 'Redemption',
    19124: 'Sanctity',
    19125: 'Theocracy',

    19286: 'CreateTradeCart',
    16655: 'Caravan',
    16657: 'Coinage_Banking',
    16659: 'Guilds',

    16696: 'Sellfood',
    16698: 'SellWood',
    16700: 'SellStone',
    16702: 'BuyFood',
    16704: 'BuyWood',
    16706: 'BuyStone',

    19321: 'Trebuchet',
    19322: 'UniqueUnit',
    19069: 'Petard',
    5375: 'FlamingCamel',
    16642: 'EliteUniqueUnit',
    16644: 'CastleUniqueTechnology',
    16646: 'ImperialUniqueTechnology',
    16648: 'Hoardings',
    16650: 'Sappers',
    16652: 'Conscription',
    16685: 'Mercenarykipchaks',

    19330: 'AutoFarms',
    16689: 'FarmUpgrade',

    19076: 'Range ',
    19077: 'Melee',
    19078: 'Archer',

    19079: 'Infantry',

    19080: 'Cavalry',

    19126: 'Arrowslits',
    19127: 'Ballistics',
    19128: 'BombardTower',
    19133: 'Chemistry',
    19129: 'FortifiedWall',
    19130: 'GuardTower',
    19131: 'HeatedShot',
    19132: 'Masonry',

    19134: 'MurderHoles',
    19135: 'SiegeEngineers',
    19136: 'TreadmillCrane',

    16784: 'Select_all_Idle_villagers',
    16785: 'Select_all_Idle_military',
    16786: 'Select_all_Trade_carts',
    16787: 'Select_all_Town_centers',
    16788: 'Select_all_Barracks',
    16789: 'Select_all_Archery ranges',
    16790: 'Select_all_Stables',
    16791: 'Select_all_Siege_workshops',
    16792: 'Select_all_Docks',
    16793: 'Select_all_Markets',
    16794: 'Select_all_Monasteries',
    16795: 'Select_all_Castles',
    16796: 'Select_all_Kreposts',
    16797: 'Select_all_Donjons',
    16798: 'Select_all_Military_Buildings',

    16687: 'WoodUpgrade',

    16692: 'GoldUpgrade',
    16694: 'StoneUpgrade',

}


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


def hotkey_assign_to_string(hotkey_assign):
    """
    stringify a hotkey assignment to be human-readable
    """
    return ("CTRL+" if hotkey_assign['ctrl'] else '') + \
           ("ALT+" if hotkey_assign['alt'] else '') + \
           ("SHIFT+" if hotkey_assign['shift'] else '') + \
           (chr(hotkey_assign['code']))


def find(char, ctrl=None, alt=None, shift=None):
    """
    find a hotkey with the given assignment
    """
    code = ord(char)
    for k, v in hkfile.hk_map.items():
        if code == v['code'] and \
                (ctrl is None or ctrl == v['ctrl']) and \
                (alt is None or alt == v['alt']) and \
                (shift is None or shift == v['shift']):
            print(k, cp_map.get(k, "UNKNOWN"))

def main():
    global hkfile
    with open(sys.argv[1]) as stringsfile:
        string_map = get_string_mapping(stringsfile)
    with open(sys.argv[2], 'rb') as hkifile:
        hki = hkifile.read()
    hkfile = hotkeys.HotkeyFile(hki, False)
    print(hkfile._file_size)
    print(hkfile.orphan_ids)
    # descs = {i: cp_map.get(i, 'UNKNOWN') for i in hkfile.orphan_ids}
    descs = {i: string_map.get(i, 'UNKNOWN') for i in hkfile.orphan_ids}
    for k, v in descs.items():
        # hotkey_str = hotkey_assign_to_string(hkfile.hk_map[k])
        # print('\'\' : (0x{:x}, {}), #{}'.format(k, repr(v), hotkey_str))
        print('\'\' : (0x{:x}, {}),'.format(k, repr(v)))

if __name__ == '__main__':
    import sys

    main()
