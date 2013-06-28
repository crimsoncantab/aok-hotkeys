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
    redirect(URL('presets', 'get', r=request))
    
    
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
    

def save():
    update_assign(json.loads(request.vars.hotkeys))
    return ''

def player1():
    response.headers['Content-Type'] = 'application/octet-stream'
    assign = update_assign(json.loads(request.vars.hotkeys))
    hkfile = load_file(assign.version)
    for hotkey, value in assign.hotkeys.items():
        if hotkey in hkfile:
            hkfile[hotkey].update(value)
    return hkfile.serialize()
    
    
def googled34aee2b940141cc():
    return open(os.path.join(request.folder, 'private', 'googled34aee2b940141cc.html')).read()
