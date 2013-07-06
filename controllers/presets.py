@arg_cache('presets')
def index():
    return response.render(dict(presets = popular_presets(0), versions={ id : name for (id, head, size, name) in hotkeys.hk_versions}))

@valid_request(str)
def get():
    p = load_preset(request.args[0])
    if not p:
        raise HTTP(404, 'Preset not found')
    #this isn't transactional, that's okay
    #usage field doesn't have to be exact
    session.assign = p.assign
    p.usage += 1
    p.update_record()
    redirect(URL('default', 'editor'))

def add():
    assign = update_assign(json.loads(request.vars.hotkeys))
    name = request.vars.name
    if not name:
        raise HTTP(400, 'Specify a name')
    if len(name) > 32:
        name = name[:32]
    preset_id = db.presets.insert(name=name, version=assign.version, assign = assign)
    cache.ram.clear('index')
    cache.ram.clear('presets')
    return URL('presets', 'get', args=str(preset_id), scheme=True, host=True)
