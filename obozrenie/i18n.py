#!/usr/bin/python
# This source file is part of Obozrenie
# Copyright 2015 Artem Vorotnikov

# For more information, see https://github.com/skybon/obozrenie

# Obozrenie is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3, as
# published by the Free Software Foundation.

# Obozrenie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Obozrenie.  If not, see <http://www.gnu.org/licenses/>.

import gettext
import locale

from obozrenie.global_settings import *

current_locale, encoding = locale.getdefaultlocale()

# gettext.bindtextdomain(APPLICATION_ID, LOCALE_DIR)
# gettext.textdomain(APPLICATION_ID)
# _ = gettext.gettext
t = gettext.translation(APPLICATION_ID, localedir=LOCALE_DIR, languages=[current_locale], codeset=encoding, fallback=True)
_ = t.gettext