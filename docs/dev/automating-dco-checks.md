# Automating DCO Checks

Checking that each commit in a merge-request has a DCO sign-off
can be automated. This should be done on the main upstream
project for a project, not on forks. That means someone with appropriate
permissions (e.g., a trustee or possibly a shop manager) must enable DCO checks.

To enable DCO checks on GitHub, enable
[Probot's DCO bot](https://probot.github.io/apps/dco/).
Then, under `Settings` and `Branches`, you must protect `master` and turn on
`Require status checks to pass before merging` and then select `DCO`.


---
Copyright (C) 2019 The LibreFoodPantry Developers.
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License". If not, see
<https://www.gnu.org/licenses/fdl-1.3.txt>.
