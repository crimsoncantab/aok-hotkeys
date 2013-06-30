def arg_cache(cache_key, time_expire=None):
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


def valid_request(*vargs, **vvars):
    """
    A decorator for validating the args and vars in a request object    
    All arguments passed to the decorator should be a type, or a tuple of the form:
    (required_type, default_value)
    """
    def decorator(method):
        def wrap():
            def valid_item(valid, item):
                has_default = type(valid) == tuple
                t = valid[0] if has_default else valid
                if not (item or has_default): raise HTTP(400) #not found if no arg and no default
                try: return t(item if item else valid[1])
                except (TypeError, ValueError):
                    log.warn('Could not cast var')
                    raise HTTP(400) #not found if we can't cast
                #TODO should be a runtime error if we can't cast the default value
            rargs = request.args
            rargs += [None]*(len(vargs)-len(rargs)) #pad rargs to be same length as vargs
            for i, varg in enumerate(vargs):
                rargs[i] = valid_item(varg, rargs[i])
            rvars = request.vars
            for k, vvar in vvars.items():
                rvars[k] = valid_item(vvar, rvars[k])
            method()
        return wrap
    return decorator
