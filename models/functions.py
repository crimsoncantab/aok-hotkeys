from gluon.contrib import simplejson as json
import hotkeys, os

#@arg_cache(cache_key = lambda n : 'presets_' + str(n))
def popular_presets(n):
    if n == 0:
        return db().select(db.presets.id, db.presets.version, db.presets.name, orderby=~db.presets.usage)
    else:
        return db().select(db.presets.id, db.presets.version, db.presets.name, orderby=~db.presets.usage, limitby=(0,n))

@arg_cache(cache_key = lambda v : 'file_{:s}'.format(v))
def load_file(version):
    return hotkeys.HotkeyFile(open(os.path.join(request.folder, 'private', 'default_{:s}.hki'.format(version))).read())

@arg_cache(cache_key = lambda v : 'version_{:s}'.format(v))
def version_hotkeys(version):
    return [k for k in hotkeys.hk_desc if k in load_file(version)]

#this can't be cached right now...
#@arg_cache(cache_key = lambda p : 'preset_' + p)
def load_preset(preset_id):
    return db.presets[preset_id]

def set_assign(hkfile):
    session.assign = hotkeys.HotkeyAssign(hkfile)

def get_assign(*args):
    if not session.assign:
        log.warn('Setting default session data')
        set_assign(load_file('22'))
    return session.assign

def update_assign(data):
    assign = get_assign()
    assign.hotkeys.update(data)
    return assign
