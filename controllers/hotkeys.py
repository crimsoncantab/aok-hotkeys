def get():
    assign = get_assign()
    #from gluon.contrib import simplejson as json
    #return json.dumps(assign.get_hotkeys(version_hotkeys(assign.version)))
    return assign.get_hotkeys(version_hotkeys(assign.version))
