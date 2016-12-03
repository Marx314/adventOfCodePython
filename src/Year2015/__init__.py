def split_data(func):
    def inner(*args, **kwargs):
        return func(args[0], args[1].split('\n'), **kwargs)
    return inner
