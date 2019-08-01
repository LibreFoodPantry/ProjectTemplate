# Commits and Their Messages

Our commit message conventions are different depending on the type of commit
we are documenting. Recall that in our workflow we work on an issue by pushing
many small commits to a feature branch associated with a merge/pull-request.
These small commits often contain incomplete implementations, experiments,
unpolished work, and even flaws. Eventually the work in our feature
branch is ready for review, and we request a review. Based on feedback, we
further refine our work by pushing more small commits to our feature branch,
and then we request another review. This continues until the reviewer(s) is
satisfied, at which point the merge/pull-request is merged into upstream's
master.

> **TIP:** We keep our merge/pull-requests and their corresponding feature
branch short-lived. The shorter the better. Ideally 1-2 days.
Keeping them short-lived reduces the risk and size of integration conflicts.
We keep them small by working hard to find simple solutions and breaking down
larger problems into many smaller problems.

Sometimes as we work on an issue, other
merge/pull-requests may be merged into master. When this happens we must
integrate those changes into our work by merging upstream's master into our
feature branch. When we do, three scenarios may occur.

1. The merge is successful, and
all the merged work passes all existing tests. In this scenario we can
continue work as normal.
2. The merge is successful,
but the merged work fails one or more tests. In this scenario we must debug
and resolve the problems pushing one or more commits until we get the merged
result passing all the tests again.
3. The merge was unsuccessful, meaning git found a lexical conflict.
In this scenario
we resolve the lexical conflicts in one or more number of commits,
run all the tests, and resolve any test failures in still more commits.

> **TIP:** We never merge master into our feature branch if we have failing
tests in our feature branch. Otherwise, figuring out if the merged work
is "good" will be difficult.

In the workflow described above, we can classify commits into three kinds:

* feature branch commits - these we make while working on a pull/merge-request
* final merge commits - these we make when a pull/merge-request is merged into
  master.
* branch synchronization commits - these we make when we merge master into
  our feature branches.


## Feature branch commit messages

Feature branches, and their associated pull/merge-request and issue,
  are used for development.
As we work on an issue, we make many small commits to the feature branch.
These commits often are not perfect. They may contain partial implementations,
experiments, unpolished work, and even flaws. As we work, we push more
small commits improving on our previous commits. We continue this until
the work is complete and until our reviewers are satisfied.

As we work on an issue, we commit and push many small commits to a
feature branch, which automatically updates a pull/merge-request that is
associated with that feature branch.
These commits aren't always perfect.
They may contain partial implementations, experiments, and mistakes.
We fix these imperfections in still more commits pushed to the same feature
branch.

For feature branch commits we make a best effort to write good commit messages,
mostly to remind ourselves what we did. They are often short and incomplete.
However, there are a two elements of these commits that are ***very*** important.

* We must have a `Signed-off-by` line to indicate that we have signed-off
  on the DCO for the contents of the commit.
* We must have a `Co-authored-by` for each co-author (other than the author)
  who helped create the commit (e.g., pair-programming or mob-programming).

These are needed to maintain the integrity of the licenses used by this project.


## Branch synchronization commits

In Git's terminology, these are "merge commits". However, these "merge commits"
serve a different purpose than what we are calling merge commits. Branch
synchronization commits are used to merge changes from master into a feature
branch, thus updating our feature branch with the newest changes in master.
There is a chance that when we merge master into our feature branch we may
need to resolve conflicts. So there are two situations, one in which we
do not have to resolve conflicts and one in which we do.

If we do not have to resolve conflicts then the we simply use the default
commit message provided by git. Nothing more is needed.

If we have to resolve conflicts then, we must provide a `Signed-off-by` line
and `Co-authored-by` lines as we do for feature branch commit messages. It is
also sometimes useful to provide some explanation about the conflicts we
resolved.


## Final merge commit messages

Final merge commits are created when our pull/merge-request is merged into master.
These commit messages summarize the changes that were made in the
  pull/merge-request.
They will be used to generate change-log messages and
  version numbers for releases.
So it's important that these commit messages are well crafted.

As we work on a merge/pull-request,
  we use its title and description to draft, review, and revise
  the final merge commit message.

The structure of these commit messages
  follow the [conventional commits](https://www.conventionalcommits.org/)
  convention.
Specifically, these commit messages have the following
  structure.


Merge commit message structure:

```
<type>[optional scope]: <description>

<body>

<footer>
```

The first line is the commit message's title/subject/header,
  and is crafted in the pull/merge-request's title.
The body and footer are crafted in the description of the pull/merge-request.


### Types

- `build` - changes to build system
- `ci` - changes to CI or CD system
- `fix` - a bug fix
- `feat` - a new feature
- `chore` - release bumps, up/down-grade 3rd party deps, etc.
- `docs` - changes to documentation
- `refactor` - changes to design
- `revert` - a commit that reverts another commit
- `perf` - changes to improve code performance
- `style` - changes to code style: whitespace, formatting, etc.
- `test` - fix or add tests for an existing feature


### Scope

The scope is optional. The scope is typically some component or feature of
  a system (e.g., `db`, `css`, `login`, `search`, `reports`, etc.).
These are project specific.


### Description

The description should be imperative, descriptive,
  and no more than 50 characters.


### Body

The body of the commit message must describe the change that was made
and why it was made.


### Footer

The footer section must contain one or more of the following lines.

* `Co-authored-by` - for each co-author who helped create this
  pull/merge-request (include all authors).
* `Closes #<issue-number>` - for each issue this pull/merge-request addresses.


---
Copyright (C) 2019 The LibreFoodPantry Developers.
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License". If not, see
<https://www.gnu.org/licenses/fdl-1.3.txt>.
