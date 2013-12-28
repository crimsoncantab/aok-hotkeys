def arg_cache(cache_key, time_expire=0):
    def decorator(method):
        def wrap(*args, **kwargs):
            try:
                key = cache_key(*args, **kwargs)
            except TypeError:
                key = str(cache_key)
            def log_wrap(*args, **kwargs):
                log.info('Caching key {:s}'.format(key))
                return method(*args, **kwargs)
            return cache.ram(key, lambda: log_wrap(*args, **kwargs), time_expire=time_expire)
        return wrap
    return decorator

def __valid_item(valid, item, key):
    has_default = type(valid) == tuple
    t = valid[0] if has_default else valid
    if item == None or item == '':
        if has_default:
            item = valid[1]
        else:
            log.warn('No value specified: {}'.format(key))
            raise HTTP(400) #not found if no arg and no default
    try:
        return item if isinstance(item, t) else t(item)
    except (TypeError, ValueError):
        log.warn('Could not cast var: {} is not castable to {}'.format(item, t))
        raise HTTP(400) #not found if we can't cast
    #TODO should be a runtime error if we can't cast the default value

def valid_request(*vargs, **vvars):
    """
    A decorator for validating the args and vars in a request object    
    All arguments passed to the decorator should be a type, or a tuple of the form:
    (required_type, default_value)
    """
    def decorator(method):
        def wrap():
            rargs = request.args
            rargs += [None]*(len(vargs)-len(rargs)) #pad rargs to be same length as vargs
            for i, varg in enumerate(vargs):
                rargs[i] = __valid_item(varg, rargs[i], i)
            rvars = request.vars
            for k, vvar in vvars.items():
                rvars[k] = __valid_item(vvar, rvars[k], k)
            method()
        return wrap
    return decorator
