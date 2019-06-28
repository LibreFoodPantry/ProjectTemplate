Contributing
============

Copyright and Licensing
-----------------------

* License for code - GPLv3
* License for content and documentation - GFDLv1.3
* Giving credit in commits
* Developer Certificate of Origin (DCO)

TODO: Each of the above need elaboration.

### Developer Certificate of Origin

Before a contribution may be accepted by LibreFoodPantry, to ensure that each
contribution is compatible with this project's open source license, its
contributors must sign-off on the following statement about their contribution
(also found in DCO in the root directory of this project or online at
  <https://developercertificate.org/>).

    Developer Certificate of Origin
    Version 1.1

    Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
    1 Letterman Drive
    Suite D4700
    San Francisco, CA, 94129

    Everyone is permitted to copy and distribute verbatim copies of this
    license document, but changing it is not allowed.


    Developer's Certificate of Origin 1.1

    By making a contribution to this project, I certify that:

    (a) The contribution was created in whole or in part by me and I
        have the right to submit it under the open source license
        indicated in the file; or

    (b) The contribution is based upon previous work that, to the best
        of my knowledge, is covered under an appropriate open source
        license and I have the right under that license to submit that
        work with modifications, whether created in whole or in part
        by me, under the same open source license (unless I am
        permitted to submit under a different license), as indicated
        in the file; or

    (c) The contribution was provided directly to me by some other
        person who certified (a), (b) or (c) and I have not modified
        it.

    (d) I understand and agree that this project and the contribution
        are public and that a record of the contribution (including all
        personal information I submit with it, including my sign-off) is
        maintained indefinitely and may be redistributed consistent with
        this project or the open source license(s) involved.

Contributors sign-off on this statement by adding a `Signed-off-by` line in
the commit message for each (co)author on the commit:
e.g., `Signed-off-by: Armadillo Aardvark <Armadillo.Aardvark@earth.com>`.
This is conveniently done if the commit is by a single author by using
the `-s` option to `git commit`: e.g., `git commit -s`.
If you need to add `Co-authored-by` lines,
manually add a `Signed-off-by` line for each co-author. Note that the
names and emails on the `Signed-off-by` lines must match the `Author`
and `Co-authored-by` lines.


Using the Issue Tracker
-----------------------

We use the issue tracker for the following:

* Bug reports
* Feature requests
* Questions
* Discussions
* Offering contributions (pull-requests)
* Reviewing contributions
* Tasks


### Bug Reports

* Report a bug
    * Provide instructions to reproduce the failure
    * Describe or show the current undesirable result
    * Describe or show the desired result
    * Be prepared to answer questions to help others to reproduce
      and diagnose the failure
* Upvote a bug report
    * If you too are impacted by the bug and would like to see it fixed.
* Evaluate a bug
    * Determine if the bug has a workaround.
    * Determine if the bug causes data loss.
    * Determine if the bug prevents a mission critical functionality.
    * Determine if the bug is a security threat.
    * Determine the environment the failure was observed in:
      i.e., production, staging, developer tests.
    * Determine the version of the project the failure was observed in.
    * Determine the platform the failure was observed in.
* Verify a bug
    * Follow instructions to reproduce the failure and report result
    * If you couldn't reproduce the failure, ask questions that might
      help you reproduce it.
* Convert a bug into a question
    * When the bug is determined to be operator error, relabel the bug as a
      question and help to answer the question.
* Diagnose a bug
    * Use debuggers, loggers, print statements, etc. to identify the fault
      that is causing the failure.
    * You may need to ask more clarifying questions.
* Propose a fix
    * Describe a possible way to fix the bug.
    * Analyze the effort needed to make this fix.
    * Analyze the overall impact of the fix on the project.
* Fix a bug
    * Follow the standard workflow for contributing code:
      fork, clone, branch, pull-request, test/code/commit/push,
      request review & merge.
* Close a bug
    * When the bug is a duplicate of another bug report.
    * When the bug is fixed and the fix is merged into master.
    * When no one has been able to reproduce the failure.
    * When the fault is outside the scope of the project.
    * When the fault exists in an unmaintained version of the project.
* Reopen a bug
    * When it is determined that a bug was closed prematurely.


### Feature Requests

* Request a feature
    * Provide a short title
    * Identify the user role who will benefit by the feature
    * Identify the feature
    * Identify the benefit to the user if the feature is implemented.
    * Consider using the following format:
      As a <user role> I want <feature>, so that <benefit>.
    * Be prepared to answer questions, provide more details, provide feedback
      on ideas, and help define acceptance criteria.
* Upvote a feature
    * If you too would like this feature, upvote the description of the feature.
* Analyze a feature
    * Identify acceptance criteria.
    * Describe how the feature might be implemented.
    * Analyze the effort involved.
    * Analyze the overall impact on the project.
    * Confirm all of the above with the requester.
* Implement a feature
    * Follow the standard workflow for contributing code:
      fork, clone, branch, pull-request, test/code/commit/push,
      request review & merge.
* Close a feature
    * When the feature has been implemented and merged into master.
    * When the feature is determined to be out of current scope of the project.
    * When the feature has been identified as a duplicate of another request.


### Questions

* Ask a question
    * Explain what you are trying to do.
    * Explain why you want to do that.
    * Identify what you have read so far.
    * Describe what you have tried so far and those results.
    * Be prepared to answer followup questions and provide more information upon request.
* Upvote a question
    * When you have the same question.
* Answer a question
    * Request more information as needed.
    * Help the original poster as much as possible.
* Upvote an answer
    * When it solved the problem for you.
* Convert to a bug report
    * When the original poster's question is really a bug.
* Convert to a feature request
    * When what the original poster wants to do is not possible.
* Add bug report on documentation
    * When existing documentation is flawed.
* Add feature request on documentation
    * When existing documentation is inadequate.
* Close a question
    * When the question has been answered.
* Reopen a question
    * When the answer was insufficient.


### Discussions

Discussions may be used to discuss changes in scope, policies, etc. They may
lead to feature requests or bug reports when decisions are made.


Finding and working on something
--------------------------------

* If there isn't an issue for the work you want to do, create one. This could be a pull-request or a plain issue.
* If an issue hasn't been discussed and has not been prioritized (check the issue's labels or its place on a project boards) by a project maintainer, start a discussion on the card. This has several goals: 1) ensure the issue has the support of a maintainer, 2) clarify the issue's context, 3) establish acceptance criteria, 4) sketch out an acceptable solution strategy, and 5) convey to others that you are interested in working on the issue.  Working on something without doing this step may lead to a waste in effort. You may work on something that will not be accepted by a maintainer.  Having this discussion reduces the risk that your
* If the issue is not claimed, claim it. You can do this in three ways; 1) if you are contributor on the project, you can assign the issue to yourself, 2) if you aren't a contributor on the project, you can leave a comment that says that you are claiming the issue, or 3) open a (draft) pull-request that claims that it closes the issue (using [GitHub's keywords](https://help.github.com/en/articles/closing-issues-using-keywords) in the pull-request). The latter is preferred as it also provides a place to observe and discuss implementation.
* If an issue has been claimed (look for an assignment, a comment, or a linked pull-request), check if it is done (merged into master). If so, close it. If you can't close it, [prompt a maintainer](https://github.blog/2011-03-23-mention-somebody-they-re-notified/) to close it. If the work isn't done, and hasn't been worked on in a while, [ask the person](https://github.blog/2011-03-23-mention-somebody-they-re-notified/) who was working on it if they are still working on it. If they aren't, then you can claim it and start working on it. If so, maybe you can help them.
* Push to your pull-request regularly. This let's others know that you are working on it. Others can also give you feedback as you go. Your pull request is a great place to get help if you get stuck.
* If you give up, leave a comment on the issue explaining the problem and indicating that you are abandoning your effort. Be sure to unclaim it (e.g., leave a comment saying you give up, unassign it, and/or close your pull-request without merging it). That way someone else can claim it.


### Offering contributions (code or documentation)

* Follow a fork-pull-request model
    * See [Forking](https://guides.github.com/activities/forking/)
    * See [GitHub Flow](https://guides.github.com/introduction/flow/)
    * See [GitHub Standard Fork & Pull Request Workflow](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
* Claim issues by either assigning it to yourself, leaving a comment stating that you are working on it, or (preferred) by creating a pull-request early and autolink to the issue in your merge-request description
    * See [Introducing Draft Pull-Requests](https://github.blog/2019-02-14-introducing-draft-pull-requests/)
    * See [Autolinked references and URLs](https://help.github.com/en/articles/autolinked-references-and-urls)
    * See [Closing issues using keywords](https://help.github.com/en/articles/closing-issues-using-keywords)
* Un-claim an issue if you stop working on an issue by closing your pull-request.
* Get feedback on your work by mentioning users you would like to review your work in a comment on your pull-request
    * See [Mention @sombody. They are notified.](https://github.blog/2011-03-23-mention-somebody-they-re-notified/)
* Mark pull-requests as "ready for review" (i.e., not a draft) and ask for a review by mentioning users on your pull-requests
    * See [Changing the status of a pull-request](https://help.github.com/en/articles/changing-the-stage-of-a-pull-request)
* Provide feedback on others work by commenting on pull-requests and/or commits on pull-requests.


### Reviewing contributions (code or documentation)

TODO: Need a checklist
* https://nyu-cds.github.io/effective-code-reviews/03-checklist/
* https://www.evoketechnologies.com/blog/code-review-checklist-perform-effective-code-reviews/
* https://medium.com/@andreigridnev/examples-of-code-review-checklists-and-guides-2dfed082a86d
* https://hackernoon.com/writing-an-amazing-code-review-checklist-de65479e8524
* https://www.codacy.com/blog/how-to-create-the-perfect-code-review-checklist/


### Tasks

Tasks are used by teams to break down the implementation of a story into a
set of tasks that can be completed by the team. In general, unless you are
part of the team that created the task, you should probably leave the task
alone. With one exception, stale tasks (> 2 month old) should be closed.
