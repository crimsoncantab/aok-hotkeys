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
        def wrap(*a, **kw):
            rargs = request.args
            rargs += [None]*(len(vargs)-len(rargs)) #pad rargs to be same length as vargs
            for i, (rarg, varg) in enumerate(zip(list(rargs), vargs)):
                if not (rarg or (type(varg) == tuple and len(varg) == 2)): raise HTTP(404) #not found if no arg and no default
                try: rargs[i] = varg[0](rarg if rarg else varg[1])
                except (TypeError, ValueError): raise HTTP(400) #not found if we can't cast
                #TODO should be a runtime error if we can't cast the default value
            rvars = request.vars
            for k, vvar in vvars:
                rvar = rvars[k]
                if not (rvar or (type(vvar) == tuple and len(vvar) == 2)): raise HTTP(400) #not found if no arg and no default
                try: rvars[k] = vvar[0](rvar if rvar else vvar[1])
                except (TypeError, ValueError): raise HTTP(400) #not found if we can't cast
                #TODO should be a runtime error if we can't cast the default value
        return wrap
    return decorator
