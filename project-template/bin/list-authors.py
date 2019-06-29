#!/usr/bin/env python3

# Copyright (C) 2019 The LibreFoodPantry Developers.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import re


author_pat = re.compile(r'^\s*author:\s+(.+)\s+(<.+>)?.*', re.IGNORECASE)
coauthor_pat = re.compile(r'\s*co-authored-by:\s+(.+)\s+(<.+>)?.*', re.IGNORECASE)

log = os.popen('git log').read()
lines = log.split('\n')

authors = []
for line in lines:
    match = author_pat.match(line)
    if match is not None:
        authors.append(match.group(1))
    match = coauthor_pat.match(line)
    if match is not None:
        authors.append(match.group(1))

for name in sorted(set(authors)):
    print(name)
