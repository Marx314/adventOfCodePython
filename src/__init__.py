def split_data(func):
    def inner(*args, **kwargs):
        if len(args) == 1:
            return func(args[0].split('\n'), **kwargs)
        else:
            return func(args[0], args[1].split('\n'), **kwargs)

    return inner
