Shop Managers
=============

Becoming a Shop Manager
-----------------------

To become a shop manager, petition the coordinating committee for membership.

**Shop Manager Petition contents**
* Full name
* Email
* Organization
* List of the project(s) that they propose to work on.
* The composition, structure, and organization of the shop (number of developers, experience of developers, and frequency of meetings)
* Agree to uphold the values of LibreFoodPantry
* Agree to regularly attend coordinating committee meetings
* Agree to join and participate in community communication channels; currently:
    * librefoodpantry-coordinating-committee@googlegroups.com
    * librefoodpantry@googlegroups.com
    * LibreFoodPantry workspace on Gitter
* If the existing meeting time for the coordinating committee does not work for the individual, a list of days and times that would.

The coordinating committee reviews the petition and determines whether to
appoint the applicant as a shop manager.


Contributing as a Shop
----------------------

This is a guide for Shop Managers who are managing a shop of developers that are working closely together to contribute to one or more LFP projects. As an agile organization, these guidelines are just that, guides. Managers and their shop may select their tools and processes as best fits their interactions and people. We suggest that shops make such decisions with the LFP values in mind and discuss them at coordinating committee meetings so that others are aware and may learn from them as well.

* Create an organization for your shop
* Fork LFP projects into your shop organization
* Protect the master branch from pushes in each project your shop forks
* Never accept pull-requests into master in any of your shop's forks
* Claim issues by
    * Creating a branch off of master for the issue in your shop fork
    * Create a draft pull-request from that branch in the shop fork to master in the project that mentions the issue number (autolink)
* Mark the pull-request as ready; the shop manager reviews and merges and closes the issue(s) it fixes.

To manage development in your shop, consider using the following additional practices.

Each project has a project board that is used to prepare issues for work and track their progress. They have the following columns.

* Product backlog - issues prioritized by shop manager(s)
* In sprint - issues and their claiming PRs
* Done - issues and PRs have been closed

Shop managers manage this board to track the progress of their shop and to coordinate with other shops that may be working on the same project. Shop managers prioritize issues in the product backlog and along with their teams groom the backlog to prepare issues for future work.

A shop may want to enable the issue tracker in their shop forks so that teams can task out

LFP Projects (upstream projects)
* Issue tracker - Contains user stories, technical stories, and bug reports
* Project boards
    * Product - managed by any shop owner
        * Freezer - issues that may or may not ever be worked on - optional; any issue not in one of the other columns is by default in the "freezer"
        * Backburner - issues for the next 6-8 sprints
        * Frontburner - issues for the next 2-3 sprints
        * In progress - issues with a PR (PR placed right above or below its issue)
        * Done - issues and PRs that have been closed since the last sprint
* Milestones
    * Has a title, a description, a deadline, an orderable list of issues, and a progress bar showing a summary of the closed/open status of the issues.
    * Possible uses:
        * Milestone per sprint - Issues are the stories that the team(s) committed to completing in the current sprint. Deadline is when the sprint is over.
        * Milestone per "epic" - Issues are the smaller stories/tasks that make up a larger story, which is represented by the Milestone. When completed, the smaller stories do not individually deliver value to an end-user, but together they do. In this case, the deadline does not mean much. Although it could be used to indicate that the milestone is part of a sprint with the same deadline, or a release with the same deadline (see Milestone per release).
        * Milestone per release - set of issues that will be included in the next release. The deadline is the release deadline.
* Releases
    * We use semantic versioning.
    * We release out of master with tags.
    * If a bug fix must be applied to a past release, we create a release branch from the release tag, cherry pick the fix, and create a new release number and tag on the release branch.
    * Releases earlier than the current major release will not be supported for more than two years
    * We create a new major release when at least one milestone has been completed.
