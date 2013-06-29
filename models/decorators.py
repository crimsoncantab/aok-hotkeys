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


def validate(*args, **vars):
    def decorator(method):
        def wrap(*args, **kwargs):
            for i, arg in enumerate(args):
                pass
        return wrap
    return decorator
