#!/usr/bin/env python
# This file is part of tcollector.
# Copyright (C) 2013  The tcollector Authors.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser
# General Public License for more details.  You should have received a copy
# of the GNU Lesser General Public License along with this program.  If not,
# see <http://www.gnu.org/licenses/>.

"""Common utility functions shared for Python collectors"""

from __future__ import print_function

import os
import stat
import pwd
import errno
import sys

PY3 = sys.version_info[0] > 2

# If we're running as root and this user exists, we'll drop privileges.
USER = "nobody"


def drop_privileges(user=USER):
    """Drops privileges if running as root."""
    try:
        ent = pwd.getpwnam(user)
    except KeyError:
        return

    if os.getuid() != 0:
        return

    os.setgid(ent.pw_gid)
    os.setuid(ent.pw_uid)


def is_sockfile(path):
    """Returns whether or not the given path is a socket file."""
    try:
        s = os.stat(path)
    except OSError as exc:
        if exc.errno == errno.ENOENT:
            return False
        err("warning: couldn't stat(%r): %s" % (path, exc))
        return None
    return s.st_mode & stat.S_IFSOCK == stat.S_IFSOCK


def err(msg):
    print(msg, file=sys.stderr)

def is_numeric_by_unicode(s):


if PY3:
    def is_numeric(value):
        
        return isinstance(value, (int, float))
else:
    def is_numeric(value):
        try:
            float(str(value))
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(value)
            return True
        except (TypeError, ValueError):
            pass

        return False
