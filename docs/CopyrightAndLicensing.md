Copyright and Licensing
=======================

Each LFP project shall use the same licenses.
For source code, the license shall be GPLv3.
For documentation and content, the license shall be GFDLv1.3.


Applying GPLv3 to source code
-----------------------------

Each project shall keep a single LICENSE file in its root
that contains the full text of the GPLv3.

Each project shall place and maintain a single AUTHORS file in its root
that contains a list of all contributors to the project.

Each project shall place at the *top* of each source code file,
in comments the following statement:

    Copyright (C) YEAR The LibreFoodPantry Developers.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


Applying FDLv1.3 to content and documentation
---------------------------------------------

Each project shall keep a single LICENSE_FOR_CONTENT file in its root
that contains the full text of the GFDLv1.3.

Each project shall place and maintain a single AUTHORS file in its root
that contains a list of all contributors to the project.

Each project shall place at the *bottom* of each document file,
the following statement:

    Copyright (c) YEAR The LibreFoodPantry Developers.
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3
    or any later version published by the Free Software Foundation;
    with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
    A copy of the license is included in the section entitled "GNU
    Free Documentation License". If not, see
    <https://www.gnu.org/licenses/fdl-1.3.txt>.


Generating AUTHORS from `git log`
---------------------------------

We have provided a Python3 script `bin/generate-authors.py` that may be used
to generate the AUTHORS file from `git log`. Run it from the root of the
project as follows.

    $ bin/generate-authors.py

If you are satisfied by its output, run it again and redirect its output
to AUTHORS.

    $ bin/generate-authors.py > AUTHORS


---
Copyright (c) 2019 The LibreFoodPantry Developers.
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License". If not, see
<https://www.gnu.org/licenses/fdl-1.3.txt>.
