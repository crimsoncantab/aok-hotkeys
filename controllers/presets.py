@arg_cache(cache_key = lambda : 'presets')
def index():
    return response.render(dict(presets = popular_presets(0), versions={ id : name for (id, head, size, name) in hotkeys.hk_versions}))

def preset():
    preset_id = request.args[0] if len(request.args) else 0
    p = load_preset(preset_id)
    if not p:
        raise HTTP(404, 'Preset not found')
    #this isn't transactional, that's okay
    #usage field doesn't have to be exact
    session.assign = p.assign
    p.usage += 2
    p.update_record()
    redirect(URL('editor'))
