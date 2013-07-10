from gluon.contrib import simplejson as json

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

@request.restful()
def api():
    response.view='generic.json'
    @arg_cache('test')
    def GET(*args, **vars):
        patterns = [
            '/p[presets]',
            '/p/{presets.id}'
        ]
        parser = db.parse_as_rest(patterns, args, vars)
        if parser.status == 200:
            return dict(content = parser.response)
        else:
            raise HTTP(parser.status, parser.error)
    return locals()

def valid_add_preset(form):
    hotkeys.update(form.vars.hotkeys)
    form.vars.assign=hotkeys.HotkeyAssign(load_file(form.vars.version))
    form.vars.assign.hotkeys.update(json.loads(request.vars.hotkeys))

def addtest():
    form = FORM(
              INPUT(_placeholder='Preset Name:', _name='name', requires=IS_NOT_EMPTY()),
              INPUT(_value='Create Preset', _type='submit'),
              INPUT(_name='hotkeys', _id='p_hotkeys', _type='hidden', requires=IS_NOT_EMPTY()),
              INPUT(_name='version', _id='p_version', _type='hidden', requires=IS_NOT_EMPTY()),
              onvalidation=valid_add_preset,
              _onsubmit="$('#p_hotkeys').val(serialize_hotkeys()); $('#p_version').val($('#versions').val());"
              )
    form.vars.hotkeys = request.vars.hotkeys
    if form.accepts(request, session):
        log.info("Adding preset called {}".format(form.vars.name))
        preset_id = db.presets.insert(name=form.vars.name, version=form.vars.version, assign=form.vars.assign)
        return dict(form=form, preset=URL('presets', 'get', args=str(preset_id), scheme=True, host=True))
    return dict(form=form)
