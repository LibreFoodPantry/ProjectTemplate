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


import sys
from datetime import datetime
from pathlib import Path


def main():
    apply_to_all_files(Path('.'), maybe_resolve_copyright_year)


def maybe_resolve_copyright_year(a_file):
    LANGLE = '<'
    RANGLE = '>'
    pattern = 'Copyright (C) ' + LANGLE + 'YEAR' + RANGLE
    with a_file.open() as f:
        content = f.read()
    if pattern in content:
        response = input(f'Resolve copyright year in {a_file} [yN]? ')
        if response == 'y':
            year = datetime.now().year
            content = content.replace(pattern, f'Copyright (C) {year}')
            print('Resolving to', a_file)
            a_file.open('w').write(content)


def apply_to_all_files(root, func):
    for f in root.iterdir():
        if f.is_file() and '.git/' not in str(f):
            func(f)
    for d in root.iterdir():
        if d.is_dir() and '.git/' not in str(d):
            apply_to_all_files(d, func)


if __name__ == '__main__':
    main()
