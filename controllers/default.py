# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    #response.flash = T("Welcome to web2py!")
    import hotkeys
    return dict(hk_desc = [(hk, hotkeys.hk_desc[hk]) for hk in hotkeys.hk22_order])

def intify(s):
    try:
        return int(s) % 256
    except:
        return 0

def hki():
    import hotkeys, hkizip, os
    hks = { k : (intify(v), 0, 0, 0) for k,v in request.post_vars.items()}
    path=os.path.join(request.folder,'private','default.txt')
    data = bytearray(open(path, 'rb').read())
    hotkeys.set_hotkeys(data, **hks)
    return hkizip.compress(str(data))
