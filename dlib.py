r"""Wrapper for bencoding_decode.h

Generated with:
D:\Python37\Scripts\ctypesgen -I ../dtorr/include -L . -ldtorr.dll ../dtorr/include/dtorr/bencoding_decode.h ../dtorr/include/dtorr/bencoding_encode.h ../dtorr/include/dtorr/dtorr.h ../dtorr/include/dtorr/fs.h ../dtorr/include/dtorr/metadata.h ../dtorr/include/dtorr/structs.h -o dlib.py --output-language=py32

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = ['.']

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs(['.'])

# Begin libraries
_libs["dtorr.dll"] = load_library("dtorr.dll")

# 1 libraries
# End libraries

# No modules

SOCKET = c_uint# ../dtorr/include/dtorr/structs.h: 15

# ../dtorr/include/dtorr/structs.h: 19
class struct_dtorr_node(Structure):
    pass

struct_dtorr_node.__slots__ = [
    'type',
    'value',
    'len',
]
struct_dtorr_node._fields_ = [
    ('type', c_int),
    ('value', POINTER(None)),
    ('len', c_ulong),
]

dtorr_node = struct_dtorr_node# ../dtorr/include/dtorr/structs.h: 24

# ../dtorr/include/dtorr/structs.h: 26
class struct_dtorr_hashnode(Structure):
    pass

struct_dtorr_hashnode.__slots__ = [
    'key',
    'value',
]
struct_dtorr_hashnode._fields_ = [
    ('key', String),
    ('value', POINTER(None)),
]

dtorr_hashnode = struct_dtorr_hashnode# ../dtorr/include/dtorr/structs.h: 30

# ../dtorr/include/dtorr/structs.h: 32
class struct_dtorr_hashmap(Structure):
    pass

struct_dtorr_hashmap.__slots__ = [
    'elements',
    'map_size',
    'entry_count',
]
struct_dtorr_hashmap._fields_ = [
    ('elements', POINTER(POINTER(dtorr_hashnode))),
    ('map_size', c_ulong),
    ('entry_count', c_ulong),
]

dtorr_hashmap = struct_dtorr_hashmap# ../dtorr/include/dtorr/structs.h: 37

# ../dtorr/include/dtorr/structs.h: 40
class struct_dtorr_listnode(Structure):
    pass

dtorr_listnode = struct_dtorr_listnode# ../dtorr/include/dtorr/structs.h: 39

struct_dtorr_listnode.__slots__ = [
    'value',
    'next',
]
struct_dtorr_listnode._fields_ = [
    ('value', POINTER(None)),
    ('next', POINTER(dtorr_listnode)),
]

# ../dtorr/include/dtorr/structs.h: 45
class struct_dtorr_config(Structure):
    pass

struct_dtorr_config.__slots__ = [
    'log_level',
    'log_handler',
]
struct_dtorr_config._fields_ = [
    ('log_level', c_int),
    ('log_handler', CFUNCTYPE(UNCHECKED(None), c_int, String)),
]

dtorr_config = struct_dtorr_config# ../dtorr/include/dtorr/structs.h: 49

# ../dtorr/include/dtorr/structs.h: 51
class struct_dtorr_ctx(Structure):
    pass

struct_dtorr_ctx.__slots__ = [
    'config',
]
struct_dtorr_ctx._fields_ = [
    ('config', POINTER(dtorr_config)),
]

dtorr_ctx = struct_dtorr_ctx# ../dtorr/include/dtorr/structs.h: 55

# ../dtorr/include/dtorr/structs.h: 57
class struct_dtorr_file(Structure):
    pass

struct_dtorr_file.__slots__ = [
    'path',
    'cat_path',
    'length',
]
struct_dtorr_file._fields_ = [
    ('path', POINTER(dtorr_node)),
    ('cat_path', String),
    ('length', c_ulong),
]

dtorr_file = struct_dtorr_file# ../dtorr/include/dtorr/structs.h: 62

# ../dtorr/include/dtorr/structs.h: 64
class struct_dtorr_peer(Structure):
    pass

struct_dtorr_peer.__slots__ = [
    'ip',
    'port',
    'peer_id',
    's',
    'active',
    'they_choked',
    'we_choked',
    'they_interested',
    'we_interested',
    'bad',
    'bitfield',
    'out_piece_requests',
    'sent_request_count',
    'total_out_request_count',
    'in_piece_requests',
    'total_in_request_count',
    'curr_in_piece_index',
    'curr_in_piece',
]
struct_dtorr_peer._fields_ = [
    ('ip', c_char * int(64)),
    ('port', c_ushort),
    ('peer_id', c_char * int(20)),
    ('s', SOCKET),
    ('active', c_char),
    ('they_choked', c_char),
    ('we_choked', c_char),
    ('they_interested', c_char),
    ('we_interested', c_char),
    ('bad', c_char),
    ('bitfield', String),
    ('out_piece_requests', POINTER(dtorr_listnode)),
    ('sent_request_count', c_ulong),
    ('total_out_request_count', c_ulong),
    ('in_piece_requests', POINTER(dtorr_listnode)),
    ('total_in_request_count', c_ulong),
    ('curr_in_piece_index', c_ulong),
    ('curr_in_piece', String),
]

dtorr_peer = struct_dtorr_peer# ../dtorr/include/dtorr/structs.h: 88

# ../dtorr/include/dtorr/structs.h: 90
class struct_dtorr_torrent(Structure):
    pass

struct_dtorr_torrent.__slots__ = [
    'announce',
    'name',
    'piece_length',
    'pieces',
    'piece_count',
    'length',
    'files',
    'file_count',
    'infohash',
    'bitfield',
    'decoded',
    'downloaded',
    'uploaded',
    'tracker_interval_map',
    'peer_map',
    'in_piece_buf_map',
    'me',
    'active_peers',
    'active_peer_count',
    'download_dir',
    'last_peerstart_time',
    'last_requester_time',
    'last_choke_time',
]
struct_dtorr_torrent._fields_ = [
    ('announce', String),
    ('name', String),
    ('piece_length', c_ulong),
    ('pieces', String),
    ('piece_count', c_ulong),
    ('length', c_ulong),
    ('files', POINTER(POINTER(dtorr_file))),
    ('file_count', c_ulong),
    ('infohash', c_char * int(20)),
    ('bitfield', String),
    ('decoded', POINTER(dtorr_node)),
    ('downloaded', c_ulong),
    ('uploaded', c_ulong),
    ('tracker_interval_map', POINTER(dtorr_hashmap)),
    ('peer_map', POINTER(dtorr_hashmap)),
    ('in_piece_buf_map', POINTER(POINTER(c_char))),
    ('me', dtorr_peer),
    ('active_peers', POINTER(dtorr_listnode)),
    ('active_peer_count', c_ulong),
    ('download_dir', String),
    ('last_peerstart_time', c_ulong),
    ('last_requester_time', c_ulong),
    ('last_choke_time', c_ulong),
]

dtorr_torrent = struct_dtorr_torrent# ../dtorr/include/dtorr/structs.h: 122

# ../dtorr/include/dtorr/structs.h: 124
class struct_dtorr_piece_request(Structure):
    pass

struct_dtorr_piece_request.__slots__ = [
    'index',
    'begin',
    'length',
    'request_sent',
]
struct_dtorr_piece_request._fields_ = [
    ('index', c_ulong),
    ('begin', c_ulong),
    ('length', c_ulong),
    ('request_sent', c_char),
]

dtorr_piece_request = struct_dtorr_piece_request# ../dtorr/include/dtorr/structs.h: 130

# D:\\Work\\dtorr\\include\\dtorr\\bencoding_decode.h: 6
if _libs["dtorr.dll"].has("bencoding_decode", "cdecl"):
    bencoding_decode = _libs["dtorr.dll"].get("bencoding_decode", "cdecl")
    bencoding_decode.argtypes = [POINTER(dtorr_config), String, c_ulong]
    bencoding_decode.restype = POINTER(dtorr_node)

# D:\\Work\\dtorr\\include\\dtorr\\bencoding_encode.h: 6
if _libs["dtorr.dll"].has("bencoding_encode", "cdecl"):
    bencoding_encode = _libs["dtorr.dll"].get("bencoding_encode", "cdecl")
    bencoding_encode.argtypes = [POINTER(dtorr_config), POINTER(dtorr_node), POINTER(c_ulong)]
    if sizeof(c_int) == sizeof(c_void_p):
        bencoding_encode.restype = ReturnString
    else:
        bencoding_encode.restype = String
        bencoding_encode.errcheck = ReturnString

# D:\\Work\\dtorr\\include\\dtorr\\dtorr.h: 6
if _libs["dtorr.dll"].has("dtorr_init", "cdecl"):
    dtorr_init = _libs["dtorr.dll"].get("dtorr_init", "cdecl")
    dtorr_init.argtypes = [POINTER(dtorr_config)]
    dtorr_init.restype = POINTER(dtorr_ctx)

# D:\\Work\\dtorr\\include\\dtorr\\dtorr.h: 8
if _libs["dtorr.dll"].has("dtorr_free", "cdecl"):
    dtorr_free = _libs["dtorr.dll"].get("dtorr_free", "cdecl")
    dtorr_free.argtypes = [POINTER(dtorr_ctx)]
    dtorr_free.restype = None

# D:\\Work\\dtorr\\include\\dtorr\\fs.h: 6
if _libs["dtorr.dll"].has("init_torrent_files", "cdecl"):
    init_torrent_files = _libs["dtorr.dll"].get("init_torrent_files", "cdecl")
    init_torrent_files.argtypes = [POINTER(dtorr_config), POINTER(dtorr_torrent)]
    init_torrent_files.restype = c_int

# D:\\Work\\dtorr\\include\\dtorr\\fs.h: 8
if _libs["dtorr.dll"].has("rw_piece", "cdecl"):
    rw_piece = _libs["dtorr.dll"].get("rw_piece", "cdecl")
    rw_piece.argtypes = [POINTER(dtorr_config), POINTER(dtorr_torrent), c_ulong, String, c_ulong, c_char]
    rw_piece.restype = c_int

# D:\\Work\\dtorr\\include\\dtorr\\metadata.h: 6
if _libs["dtorr.dll"].has("load_torrent_metadata", "cdecl"):
    load_torrent_metadata = _libs["dtorr.dll"].get("load_torrent_metadata", "cdecl")
    load_torrent_metadata.argtypes = [POINTER(dtorr_config), String, c_ulong]
    load_torrent_metadata.restype = POINTER(dtorr_torrent)

# D:\\Work\\dtorr\\include\\dtorr\\metadata.h: 8
if _libs["dtorr.dll"].has("free_torrent", "cdecl"):
    free_torrent = _libs["dtorr.dll"].get("free_torrent", "cdecl")
    free_torrent.argtypes = [POINTER(dtorr_torrent)]
    free_torrent.restype = None

# ../dtorr/include/dtorr/structs.h: 4
try:
    DTORR_DICT = 1
except:
    pass

# ../dtorr/include/dtorr/structs.h: 5
try:
    DTORR_STR = 2
except:
    pass

# ../dtorr/include/dtorr/structs.h: 6
try:
    DTORR_LIST = 3
except:
    pass

# ../dtorr/include/dtorr/structs.h: 7
try:
    DTORR_NUM = 4
except:
    pass

dtorr_node = struct_dtorr_node# ../dtorr/include/dtorr/structs.h: 19

dtorr_hashnode = struct_dtorr_hashnode# ../dtorr/include/dtorr/structs.h: 26

dtorr_hashmap = struct_dtorr_hashmap# ../dtorr/include/dtorr/structs.h: 32

dtorr_listnode = struct_dtorr_listnode# ../dtorr/include/dtorr/structs.h: 40

dtorr_config = struct_dtorr_config# ../dtorr/include/dtorr/structs.h: 45

dtorr_ctx = struct_dtorr_ctx# ../dtorr/include/dtorr/structs.h: 51

dtorr_file = struct_dtorr_file# ../dtorr/include/dtorr/structs.h: 57

dtorr_peer = struct_dtorr_peer# ../dtorr/include/dtorr/structs.h: 64

dtorr_torrent = struct_dtorr_torrent# ../dtorr/include/dtorr/structs.h: 90

dtorr_piece_request = struct_dtorr_piece_request# ../dtorr/include/dtorr/structs.h: 124

# No inserted files

# No prefix-stripping

