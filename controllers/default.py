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
    #TODO - memcache the list comprehension?
    return dict(hk_desc = [(group, [(hk, hotkeys.hk_desc[hk]) for hk in hks]) for (group, hks) in hotkeys.hk_groups])

def load_file(name):
    return hotkeys.HotkeyFile(open(os.path.join(request.folder, 'private', name + '.hki')).read())
    
def get_file(*args):
    if not session.hkfile:
        session.hkfile = load_file('default')
    return session.hkfile

def copy_dict(d, *keys):
    return {key: d[key] for key in keys}

def recall():
    hkfile = get_file()
    from gluon.contrib import simplejson as json
    return json.dumps({k:copy_dict(v,'code', 'ctrl', 'alt', 'shift') for (k,v) in hkfile})
    
def setfile():
    f = request.args[0] if request.args else 'default'
    
    if f == 'upload' and 'hki' in request.vars:
        hkfile = hotkeys.HotkeyFile(request.vars.hki.file.getvalue())
    elif f == 'none':
        hkfile = load_file('none')
    elif f == 'default20':
        hkfile = load_file('default20')
    else:
        hkfile = load_file('default')
    session.hkfile = hkfile
    redirect(URL(editor))

def update_hkfile(data):
    hkfile = get_file()
    for hotkey, value in data.items():
        #del value['id'] # need to do this?
        hkfile[hotkey].update(value)
    return hkfile


def save():
    update_hkfile(json.loads(request.vars.hotkeys))
    return ''

def player1():
    return update_hkfile(json.loads(request.vars.hotkeys)).serialize()
    
    
def googled34aee2b940141cc():
    return open(os.path.join(request.folder, 'private', 'googled34aee2b940141cc.html')).read()
