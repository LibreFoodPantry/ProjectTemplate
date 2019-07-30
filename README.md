# Project Template
<!-- Replace the above with your project's title. -->

<!-- Brief description of the project and the problem it solves. -->
This is a template for LFP projects.
It can be used when starting a new project,
or to update an existing project with standard LFP project files.


## Requirements

<!--
List of direct dependencies.
Only constrain version numbers if it is known that this project cannot work with
particular versions.
-->

- Python 3.6+ for the scripts in bin/

## Quick Start

<!--
A short example of installing, running, and using with minimal explanation.
-->

### Start a new project

Create a new project in GitLab or GitHub without any initial content, and then:

```bash
$ git clone https://github.com/LibreFoodPantry/ProjectTemplate.git <YourNewProject>
$ cd YourNewProject
$ git remote set-url origin <UrlOfYourNewProject>
$ git push -u origin master
```

### Integrate with an existing project

The idea is to [merge two projects with no common history](https://thoughts.t37.net/merging-2-different-git-repositories-without-losing-your-history-de7a06bba804),
resolving any conflicts as sanely as possible,
and removing unneeded files.

### Updating a project with new changes from this project

If your project was started using one of the processes described above,
the you can get new changes by fetching and merging changes from this project
as follows (using a feature branch and merge request, of course):

```bash
$ git clone <UrlOfYourProject>        # Clone your project
$ cd <YourProject>                    # Move into your project
$ git remote add template https://github.com/LibreFoodPantry/ProjectTemplate.git   # Add a remote to this project
$ git fetch template                  # Fetch changes from template
$ git checkout -b <FeatureBranch>     # Create a feature branch
$ git merge template/master           # Merge changes from template/master into feature branch; resolve conflicts carefully
$ git push -u origin <FeatureBranch>  # Push feature branch for review
```

Now issue a merge request back to your master and request a review.


### Modifying files

Once you have based your project on this project, you should customize the following files:

- README.md (this one)
- CONTRIBUTING.adoc


## Contributing

Want to help? Great! Please see [CONTRIBUTING](CONTRIBUTING.adoc).

---
Copyright (c) <YEAR> The LibreFoodPantry Developers.
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License". If not, see
<https://www.gnu.org/licenses/fdl-1.3.txt>.
