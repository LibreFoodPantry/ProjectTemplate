# Resolve Years in Copyright Notices

The provided copyright snippets contain a placeholder for the year: &lt;YEAR\>.
You can either manually replace this with the current year, or you can use
the `resolve-copyright-years.py` script.

When you run `resolve-copyright-years.py` in the root of the project,
it searches all files in the project for the &lt;YEAR\> placeholder. For each
file it finds with this placeholder, it asks you if you want to replace it with
the current year.

```bash
$ bin/resolve-copyright-years.py
src/main.py [yN]? y
Resolving to src/main.py
...
```

---
Copyright (c) 2019 The LibreFoodPantry Developers.
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License". If not, see
<https://www.gnu.org/licenses/fdl-1.3.txt>.
