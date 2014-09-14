# testing/mock.py
# Copyright (C) 2005-2014 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""Import stub for mock library.

    NOTE:  copied/adapted from SQLAlchemy master for backwards compatibility;
   this should be removable when Alembic targets SQLAlchemy 0.9.4.

"""
from __future__ import absolute_import
from alembic.compat import py33

if py33:
    from unittest.mock import MagicMock, Mock, call, patch
else:
    try:
        from mock import MagicMock, Mock, call, patch
    except ImportError:
        raise ImportError(
            "SQLAlchemy's test suite requires the "
            "'mock' library as of 0.8.2.")