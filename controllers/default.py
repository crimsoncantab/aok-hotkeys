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

def cacheversion():
    for v in [v[0] for v in hotkeys.hk_versions]:
        load_file(v)
        version_hotkeys(v)
    return 'Data cached'

@arg_cache(cache_key = lambda : 'index')
def index():
    return response.render(dict(presets = popular_presets(10), versions = { id : name for (id, head, size, name) in hotkeys.hk_versions}))

@arg_cache(cache_key = lambda : 'editor_{:s}'.format(get_assign().version))
def editor():
    return response.render(dict(
                hk_desc = [(group, [(hk, hotkeys.hk_desc[hk]) for hk in hks]) for (group, hks) in hotkeys.hk_groups],
                hk_versions = hotkeys.hk_versions, version = get_assign().version
                ))

def recall():
    assign = get_assign()
    from gluon.contrib import simplejson as json
    return json.dumps(assign.get_hotkeys(version_hotkeys(assign.version)))
    
def version():
    if request.vars.version not in [v[0] for v in hotkeys.hk_versions]:
        raise HTTP(400, 'Bad version specified')
    get_assign().version = request.vars.version

def preset():
    preset_id = request.args[0] if len(request.args) else 0
    p = load_preset(preset_id)
    if not p:
        raise HTTP(404, 'Preset not found')
    #this isn't transactional, that's okay
    #usage field doesn't have to be exact
    session.assign = p.assign
    p.usage += 1
    p.update_record()
    redirect(URL('editor'))
    
    
def upload():
    if 'hki' in request.vars and request.vars.hki != '':
        try:
            hkfile = hotkeys.HotkeyFile(request.vars.hki.file.getvalue())
        except:
            raise HTTP(400, 'File format not recognized')
    else:
        raise HTTP(400, 'File not specified')
    log.info('File version: {:s}'.format(hkfile.version))
    set_assign(hkfile)
    redirect(URL('editor'))
    

def addpreset():
    assign = update_assign(json.loads(request.vars.hotkeys))
    name = request.vars.name
    if not name:
        raise HTTP(400, 'Specify a name')
    if len(name) > 32:
        name = name[:32]
    preset_id = db.presets.insert(name=name, version=assign.version, assign = assign)
    cache.ram.clear('index')
    cache.ram.clear('getpresets')
    return URL(preset, args=str(preset_id), scheme=True, host=True)

@arg_cache(cache_key = lambda : 'getpresets')
def getpresets():
    return response.render(dict(presets = popular_presets(0), versions={ id : name for (id, head, size, name) in hotkeys.hk_versions}))

def save():
    update_assign(json.loads(request.vars.hotkeys))
    return ''

def player1():
    response.headers['Content-Type'] = 'application/octet-stream';
    assign = update_assign(json.loads(request.vars.hotkeys))
    hkfile = load_file(assign.version)
    for hotkey, value in assign.hotkeys.items():
        if hotkey in hkfile:
            hkfile[hotkey].update(value)
    return hkfile.serialize()
    
    
def googled34aee2b940141cc():
    return open(os.path.join(request.folder, 'private', 'googled34aee2b940141cc.html')).read()
