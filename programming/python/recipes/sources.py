import os
import importlib.machinery
import importlib.util
import sys
import glob
import time
import getopt
import token
import tokenize

__version__ = '1.5'

default_keywords = ['_']
DEFAULTKEYWORDS = ', '.join(default_keywords)

EMPTYSTRING = ''

def make_escapes(pass_nonascii):
    global escapes, escape
    if pass_nonascii:
        # Allow non-ascii characters to pass through so that e.g. 'msgid
        # "Höhe"' would result not result in 'msgid "H\366he"'.  Otherwise we
        # escape any character outside the 32..126 range.
        mod = 128
        escape = escape_ascii
    else:
        mod = 256
        escape = escape_nonascii
    escapes = [r"\%03o" % i for i in range(mod)]
    for i in range(32, 127):
        escapes[i] = chr(i)
    escapes[ord('\\')] = r'\\'
    escapes[ord('\t')] = r'\t'
    escapes[ord('\r')] = r'\r'
    escapes[ord('\n')] = r'\n'
    escapes[ord('\"')] = r'\"'


def escape_ascii(s, encoding):
    return ''.join(escapes[ord(c)] if ord(c) < 128 else c for c in s)


def escape_nonascii(s, encoding):
    return ''.join(escapes[b] for b in s.encode(encoding))


def is_literal_string(s):
    return s[0] in '\'"' or (s[0] in 'rRuU' and s[1] in '\'"')


def safe_eval(s):
    # unwrap quotes, safely
    return eval(s, {'__builtins__':{}}, {})

def normalize(s, encoding):
    # This converts the various Python string types into a format that is
    # appropriate for .po files, namely much closer to C style.
    lines = s.split('\n')
    if len(lines) == 1:
        s = '"' + escape(s, encoding) + '"'
    else:
        if not lines[-1]:
            del lines[-1]
            lines[-1] = lines[-1] + '\n'
        for i in range(len(lines)):
            lines[i] = escape(lines[i], encoding)
        lineterm = '\\n"\n"'
        s = '""\n"' + lineterm.join(lines) + '"'
    return s

def containsAny(str, set):
    """Check whether 'str' contains ANY of the chars in 'set'"""
    return 1 in [c in str for c in set]

print(containsAny("test?", "*?[]"))
print(containsAny("test", "*?[]"))

def getFilesForName(name):
    """Get a list of module files for a filename, a module or package name,
    or a directory.
    """
    if not os.path.exists(name):
        # check for glob chars
        if containsAny(name, "*?[]"):
            files = glob.glob(name)
            list = []
            for file in files:
                list.extend(getFilesForName(file))
            return list

        # try to find module or package
        try:
            spec = importlib.util.find_spec(name)
            name = spec.origin
        except ImportError:
            name = None
        if not name:
            return []

    if os.path.isdir(name):
        # find all python files in directory
        list = []
        # get extension for python source files
        _py_ext = importlib.machinery.SOURCE_SUFFIXES[0]
        for root, dirs, files in os.walk(name):
            # don't recurse into CVS directories
            if 'CVS' in dirs:
                dirs.remove('CVS')
            # add all *.py files to list
            list.extend(
                [os.path.join(root, file) for file in files
                 if os.path.splitext(file)[1] == _py_ext]
                )
        return list
    elif os.path.exists(name):
        # a single file
        return [name]

    return []