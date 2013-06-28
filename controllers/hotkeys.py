def get():
    assign = get_assign()
    #from gluon.contrib import simplejson as json
    #return json.dumps(assign.get_hotkeys(version_hotkeys(assign.version)))
    return assign.get_hotkeys(version_hotkeys(assign.version))

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
    redirect(URL('default', 'editor'))
