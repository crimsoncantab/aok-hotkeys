# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
from gluon.contrib import simplejson as json
import hotkeys, os

def index():
    return dict()

def editor():
    v = get_assign().version
    return cache.ram('editor_' + v, lambda: response.render(dict(
                hk_desc = [(group, [(hk, hotkeys.hk_desc[hk]) for hk in hks]) for (group, hks) in hotkeys.hk_groups],
                hk_versions = hotkeys.hk_versions, version = v
                )), time_expire=None)

def load_file(name):
    filename = name + '.hki'
    return cache.ram(filename, lambda: hotkeys.HotkeyFile(open(os.path.join(request.folder, 'private', name + '.hki')).read()), time_expire=None)

def version_hotkeys(version):
    return cache.ram(version, lambda: [k for k in hotkeys.hk_desc if k in load_file('default_' + version)], time_expire=None)

def set_assign(hkfile):
    session.assign = hotkeys.HotkeyAssign(hkfile)

def get_assign(*args):
    if not session.assign:
        log.warn('Setting default session data')
        set_assign(load_file('default_22'))
    return session.assign

def update_assign(data):
    assign = get_assign()
    assign.hotkeys.update(data)
    return assign

def recall():
    assign = get_assign()
    from gluon.contrib import simplejson as json
    return json.dumps(assign.get_hotkeys(version_hotkeys(assign.version)))
    
def version():
    if request.vars.version not in hotkeys.hk_versions:
        raise HTTP(400, 'Bad version specified')
    get_assign().version = request.vars.version
    
def setfile():
    f = request.args[0] if request.args else 'default'
    
    if f == 'upload' and 'hki' in request.vars:
        if not request.vars.hki:
            raise HTTP(400, 'File not specified')
        hkfile = hotkeys.HotkeyFile(request.vars.hki.file.getvalue())
    elif f == 'none':
        hkfile = load_file('none')
    elif f == 'default20':
        hkfile = load_file('default20')
    else:
        hkfile = load_file('default')
    log.info('File version: {:s}'.format(hkfile.version))
    set_assign(hkfile)
    redirect(URL(editor))

def save():
    update_assign(json.loads(request.vars.hotkeys))
    return ''

def player1():
    response.headers['Content-Type'] = 'application/octet-stream';
    assign = update_assign(json.loads(request.vars.hotkeys))
    hkfile = load_file('default_' + assign.version)
    for hotkey, value in assign.hotkeys.items():
        if hotkey in hkfile:
            hkfile[hotkey].update(value)
    return hkfile.serialize()
    
    
def googled34aee2b940141cc():
    return open(os.path.join(request.folder, 'private', 'googled34aee2b940141cc.html')).read()
