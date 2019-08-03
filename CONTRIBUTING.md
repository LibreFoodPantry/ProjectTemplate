# Contributing

We are grateful that you want to contribute to this project!

This guide will help you determine the best way to contribute
to this project. By reading and respecting the practices in this guide, others
in the community are more likely to value and accept your contributions.


## LibreFoodPantry

This project is a [LibreFoodPantry](https://librefoodpantry.org) project.
We are a part of this larger community and share its values, policies, and resources.


## Vision

LibreFoodPantry is a vibrant, welcoming community of clients, users, and developers who believe in developing and maintaining humanitarian projects. We enhance computer science education through involvement in instructor-led, free and open source software projects that support local food pantries.


## Mission

Our mission is to expand a community of students and faculty across multiple institutions who believe software can be used to help society. We strive to support local food pantries with quality, adaptable, free and open source software (FOSS) to help them serve their guests. Through learning opportunities within FOSS food pantry projects, we provide students with the perspective that computing can be used for social good.


## Values

To ensure a healthy and safe environment in which to collaborate and learn,
and to help establish and promote effective development practices,
we have adopted the following values.
We expect all community members to read and uphold these values.

* [Code of conduct](CODE_OF_CONDUCT.md)
* Agile [values](https://agilemanifesto.org/)
  and [principles](https://agilemanifesto.org/principles.html)
* [FOSSisms](https://opensource.com/education/14/6/16-foss-principles-for-educators)


## Licensing

We license source code under [GPL v3](LICENSE.md)
and content under [GFDL v1.3](LICENSE_FOR_CONTENT.md).
For each commit, contributors must
* Include a [copyright notice](copyright-notices/) on each new file
* Sign-off on the [DCO v1.1](DCO.txt) in the commit message
* And credit all co-authors in the commit message

Please read
[Licensing](docs/dev/licensing.md)
for instructions on how to do any of the above.


## Communication

* Use GitHub's or GitLab's to "watch" issues and projects to receive
  notifications when things change. This will help you remain aware.
* Most of your communication (say 80%) should be through the issue tracker and
  issue boards (called "projects" in GitHub). Use them to report problems,
  propose features, strategize, give feedback, propose changes to policies
  and procedures, ask questions, offer changes through merge requests,
  review changes, etc. This is this preferred way to communicate as it
  allows us to organize conversations around issues and because it is public.
* Some of your communication (say 19%) should be through [#TODO chat system]
  to ask questions, schedule meetings, hold meetings,
  give or receive live help, give or receive demos or tutorials,
  socialize, etc.
* A minimum of your of your communication (say 1% or less)
  should be through email. Only use email for personal, private matters.

There are several FOSSisms at play here:

* FOSSism #1: It's all about community
* FOSSism #5: If it isn't public, it didn't happen
* FOSSism #6: Embrace radical transparency
* FOSSism #9: Keep a history
* FOSSism #16: Avoid uncommunicated work

We prefer public issue trackers over email because it is public
and transparent. We prefer issue trackers over chat communication because
it is more organized.

For more information about our issue trackers, issue boards, issues, and labels
please read [Issue Tracker](docs/dev/issue-tracker.md).

## Initial setup

At a minimum __create a GitHub and GitLab account__. This will allow you to
create and comment on issues. Choose a name and email that you are
comfortable with being public. GitHub and GitLab will identify you by
this name and email when you make and comment on issues.
They will also use this information to link your commits to your account.

If you intend to make changes you will need to __install and configure Git__.

* Download and install git from [git-scm.com](https://git-scm.com/).
* [Configure Git](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

When you configure Git, give the same name and email that you gave to GitHub
and GitLab. Again, remember this name and email will become public, as git will
include them in each commit you make, and when you contribute them, they
will be publicly visible.

Next, on GitHub or GitLab, __fork the project(s)__ you will be working on.
If you are working in a shop, your shop manager will create a shop fork.
Use this instead of creating your own. Your shop manager needs to give you
permissions to push to the shop fork.

See also [Shop Setup](docs/dev/shop-setup) for more information on development
shops and how to set one up.


## Adding issues

There are several types of issues in the issue tracker:

* Bug reports - These are undesirable behaviors that need to be fixed.
* Feature requests / User Stories - These are new desired behaviors that benefit one or more end users.
* Tech Stories - These are proposed changes that do not directly impact an end user but help improve the maintainability or development of the system.
* Spikes - These are proposed efforts to learn/discover something to help answer a question related to an issue.
* Tasks - These are small specific steps that must be completed to implement a solution for a specific issue.
* Proposals - These are general proposals for discussing anything that doesn't easily fit in any of the other types of issues (e.g., changes in policy, project scope, etc.)

Issues can and should be added at anytime during development.
If you see something, say something.

See also [Issue Tracker](docs/dev/issue-tracker.md).


## Grooming issues

Grooming is the process of prioritizing and refining issues into workable units.

* Unreproducible bug reports must be identified and closed.
* Invalid issues must be identified and closed.
* Duplicate issues need to be identified and closed.
* Stalled issues must be identified and the reason for the stall documented.
* Valuable/important issues must be raised in priority.
* Large, vague, issues must be broken into smaller more manageable issues.
  Ideally it should take 2-3 days at most to implement a solution. If an
  issue is likely to take longer a plan must be made to implement it in
  smaller stages (see #TODO link to trunk-based development's page on
  feature toggle development pattern).
* High-priority issues must be clarified and acceptance criteria defined.
* Well-defined, high-priority issues must be labelled ready.
* Issues must be labelled correctly.

All of this happens by many people reviewing issues and commenting on them.
If you see an issue that you believe deserves a higher priority,
comment on it and explain why. If you think a card is miss-labelled, comment
on it and explain why. If you see an open merge-request that hasn't been
worked on in a while and there is no information as to why work as stopped,
comment on the card and ask why. If you see a bug and no one except the
reporter has been able to reproduce, try to reproduce it yourself and report
your result. And so on.

This is an ongoing process. When you look through the issue tracker and its
boards looking for something to work on, plan to comment on issues and help
prioritize, organized, and prepare them for work.

See also [Issue Tracker](docs/dev/issue-tracker.md).


## Refining and prioritizing issues

This section overlaps with the previous. But now the assumption is that you
have identified an issue that you would like to work on. Before working on
it, you want to make sure that the issue is well defined, is small and
manageable, the community values it, and that it will likely be
accepted if you implement it. We do this through discussions on the issue.
Specifically, on the issue, you should try to ask and provide answers to
the following questions.

* What's the status of the issue? Is someone working on it? Has the effort
  stalled? If it has stalled, why? Is it blocked by another issue? If so,
  how can the issue be unblocked?
* For bugs, what is the nature of the problem?
  What is the current undesirable behavior?
  What are the steps to reproduce the undesirable behavior?
  Can you reproduce the undesirable behavior?
  What is the desired behavior?
* For feature requests, who (what user role) will benefit if the feature
  is implemented? What is the desired feature? How will that role benefit?
  What are the acceptance criteria: i.e., how specifically should the system
  behave if this feature is implemented? Can these acceptance criteria be
  implemented as automated tests?
* How desirable, important, and/or urgent is the feature or bug fix?
* How should this bug be fixed or feature implemented? What are the different
  possible implementation strategies? What are the benefits and drawbacks of
  each strategy? What is the impact of the strategy on the rest of the system?
  How much effort is required by each strategy? Can the issue be broken into
  smaller more manageable issues? If so, what would those smaller issues be?

See also [Issue Tracker](docs/dev/issue-tracker.md).


## Getting ready to work

* Claim the issue.
    * If you can, assign it to yourself (and your team members).
    * If you can't assign it to yourself
   (i.e., you don't have the appropriate permissions to do so),
   comment on the card that you and your team will work on it.
* Create a feature branch, make an empty commit, push it to your fork,
  and create a merge-request (with a WIP prefix) back to upstream's master.
  (If you are in a team only one member needs to create and publish the
    feature branch and create the merge-request;
    after, other members can simply checkout the feature branch
    in their clone of the fork.)
* If you are working in a team
    * Add the issue to your team's Sprint or Kanban board.
    * Create an initial "To Do" list on your team's board by thinking through
  all the tasks that need to get done to complete the issue.


## Work

Ideally, this stage is no longer than 2-3 days.
The longer it takes to implement the solution for an issue, the
more difficult it will be to integrate and merge the solution and
the larger the risk that the solution will never get merged.
That's why it's important to carefully groom and refine issues.

* If you are working in a team with a Sprint or Kanban board, claim a task
  in "To do" and move it to "Doing", work on it, and move it to "Done"
  when you are done. If you think of other things that need to get done,
  add them to "To do" when you think of them. Help keep the "To Do" list
  in order.
* Work on your feature branch. Make it a habit to checkout your feature branch
  each time you sit down to work.
* Sign-off on the DCO for each commit you make. This is done by adding `-s`
  to each commit: e.g., `git commit -s`.
* Credit all co-authors on each commit by including
  a `Co-authored-by: NAME <EMAIL>` line for each co-author at the bottom
  of the commit message.
* Write automated tests.
* Implement changes.
* Refactor and clean code.
* Update merge-request title and description which will become the final
  merge-commit message.
* Push changes regularly--even after each commit!
    * Others can track your progress.
    * Others may become motivated.
    * Triggers continuous integration tests and deployment to a demo
   environment. Manually test in the demo environment.


## Getting your work reviewed and merged

The last stage of contribution is getting your merge-request accepted and
merged into upstream's master. This is often the longest stage (2-4 days)
as it may require several back-and-forth asynchronous communications between
you, the reviewers, and ultimately the committing maintainer.

First, integrate any new changes from upstream's master into your feature branch.
It's important to demonstrate that your changes are compatible with any new
changes in master before it can be merged. Do this by fetching the changes
in upstream's master into your local repository's master, merging
master into your feature branch, fix any merge conflicts, and running all tests
to ensure they all pass (or make more commits until they do). Don't forget
to push your work as you go.

```
$ get checkout <FEATURE_BRANCH>       # <1>
$ git fetch upstream master:master    # <2>
$ git merge master                    # <3>
$ <test>                              # <4>
$ git add . ; git commit -m "Integrate changes from upstream/master" ; git push  # <5>
```
1. Make sure your feature branch is checked out.
2. Fetch changes in upstream's master and merge them into your local master.
    If this fails, probably your local master has diverged from upstream's
    master. This happens if you or someone else accidentally commits to
    master directly.
3. Merge master into your feature branch. This may result in merge conflicts
    which you will need to carefully resolve and commit before moving on.
4. Run all tests. You may want to do some manual testing too.
    If any tests fail, make and commit fixes until all tests pass.
5. Stage, commit, and push your work.

At this point, you should be ready for a final review. Remove the WIP status
from your merge request and request a review from one or more reviewers.
They will review your work for the following characteristics in roughly
this order:

* The DCO has been signed-off on *_each commit_* by its author
  (see [Commits and Their Messages](docs/dev/commits-and-their-messages.md))
* All tests pass.
* The merge-request title and description comprise a good final merge
  commit message (see [Commits and Their Messages](docs/dev/commits-and-their-messages.md)).
* The changes address the issues it claims to address;
  nothing more and nothing less.
* New tests are provided the test the new code that has been developed.
* The code and tests follow clean code principles and practices.
* The code and tests are well-designed and read well.
* The code and tests follow the coding conventions of this project.

After you receive a review, you should do your best to satisfy the reviewers
through discussion and making and pushing more changes to your merge-request.
This process ends when the reviewers are satisfied and mark the merge-request
to be merged (or a maintainer merges the merge-request).

Note, even after all the reviewers are satisfied, you may still need to
integrate new changes into your merge-request if other merge requests are
merged before yours.


See also [Automating DCO Checks](docs/dev/automating-dco-checks.md).

---
Copyright (C) 2019 The LibreFoodPantry Developers.
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License". If not, see
<https://www.gnu.org/licenses/fdl-1.3.txt>.
