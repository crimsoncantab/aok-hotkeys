from gluon.contrib import simplejson as json

def get():
    assign = get_assign()
    return assign.get_hotkeys(version_hotkeys(assign.version))

from cgi import FieldStorage
@valid_request(hki=FieldStorage)
def upload():
    try:
        hkfile = hotkeys.HotkeyFile(request.vars.hki.file.getvalue())
    except Exception as e:
        raise HTTP(400, 'File format not recognized: {}'.format(e.message))
    log.info('File version: {:s}'.format(hkfile.version))
    set_assign(hkfile)
    redirect(URL('default', 'editor'))

def save():
    update_assign(json.loads(request.vars.hotkeys))
    return ''

def download():
    response.headers['Content-Type'] = 'application/octet-stream'
    assign = update_assign(json.loads(request.vars.hotkeys))
    hkfile = load_file(assign.version)
    for hotkey, value in assign.hotkeys.items():
        if hotkey in hkfile:
            hkfile[hotkey].update(value)
    return hkfile.serialize()

def version():
    if request.vars.version not in [v[0] for v in hotkeys.hk_versions]:
        raise HTTP(400, 'Bad version specified')
    get_assign().version = request.vars.version
