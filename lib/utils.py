def interruptable(fn):
    import sys

    def wrap(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except KeyboardInterrupt:
            print('\n[i] Interrupted by user. Exiting.')
            sys.exit(130)
    wrap.__doc__ = fn.__doc__
    return wrap


def tim():
    from datetime import datetime
    return datetime.now().strftime('%H:%M:%S')


def dt():
    from datetime import datetime
    return datetime.now().strftime('%d.%m %H:%M:%S')


def parse_range_list(rgstr):
    """Parse ranges such as 2-5,7,12,8-11 to [2,3,4,5,7,8,9,10,11,12]"""
    import re
    from itertools import chain

    def parse_range(rg):
        if len(rg) == 0:
            return []
        parts = re.split(r'[:-]', rg)
        if len(parts) > 2:
            raise ValueError("Invalid range: {}".format(rg))
        try:
            return range(int(parts[0]), int(parts[-1])+1)
        except ValueError:
            if len(parts) == 1:
                return parts
            else:
                raise ValueError("Non-integer range: {}".format(rg))
    rg = map(parse_range, re.split(r'\s*[,;]\s*', rgstr))
    return list(set(chain.from_iterable(rg)))
