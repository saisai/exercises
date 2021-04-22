# django/core/management/commands/diffsettings.py
def module_to_dict(module, omittable=lambda k: k.startswith('_')):
    """Converts a module namespace to a Python dictionary."""
    return {k: repr(v) for k, v in module.__dict__.items() if not omittable(k)}

import time
from threading import Thread

for mo in [Thread, time]:
    print(module_to_dict(mo))


# django/core/management/commands/compilemessages.py
def has_bom(fn):
    with open(fn, 'rb') as f:
        sample = f.read(4)
    return sample.startswith((codecs.BOM_UTF8, codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE))


def is_writable(path):
    # Known side effect: updating file access/modified time to current time if
    # it is writable.
    try:
        with open(path, 'a'):
            os.utime(path, None)
    except (IOError, OSError):
        return False
    return True
