def cacheversion():
    for v in [v[0] for v in hotkeys.hk_versions]:
        load_file(v)
        version_hotkeys(v)
    return 'Data cached'

@arg_cache('index')
def index():
    log.info(type(request.args))
    return response.render(dict(presets = popular_presets(10), versions = { id : name for (id, head, size, name) in hotkeys.hk_versions}))

@arg_cache('editor_{:s}'.format(get_assign().version))
def editor():
    return response.render(dict(
                hk_desc = [(group, [(hk, hotkeys.hk_desc[hk]) for hk in hks]) for (group, hks) in hotkeys.hk_groups],
                hk_versions = hotkeys.hk_versions, version = get_assign().version
                ))

def preset():
    redirect(URL('presets', 'get', r=request))
    
def googled34aee2b940141cc():
    return open(os.path.join(request.folder, 'private', 'googled34aee2b940141cc.html')).read()
