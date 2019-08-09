# Continuous Integration and Deployment/Delivery

For a more in-depth look at CI/CD see [GitHub's video about CI](https://youtu.be/xSv_m3KhUO8)

## Continuous integration

As we work on a feature in a feature branch, others' work is being accepted
and merged into master. When we get our feature working in our feature branch,
we don't want to merge it into master until we know that our changes will
also work with the new changes in master. So before we merge our feature into
master, we must first integrate our changes with the new changes in master to
make sure they properly work together. This integration process becomes riskier
and more difficult the more master and our feature branch diverge from each
other. In fact, it can become so difficult that we may choose to abandon our
feature branch and start over! To help avoid these situations and make
integration easier, we use continuous integration.

__Continuous Integration (CI)__ is the practice of _frequently_ integrating our
work and master. By integrating our work and master several times a day
each integration becomes smaller and easier because the two branches are not
allowed to diverge too far. By the time we are "done" with our feature,
the final integration should be just another small integration.

GitLab can be enabled to help us with CI. When CI checks are enabled,
GitLab checks if a merge request's feature branch can
be safely merged with master each time we push a commit to the feature branch.
GitLab does this by merging master and our feature branch into a separate
temporary branch and then runs the projects automated tests on
the temporary branch. GitLab reports the results of merging and testing to
the merge request. GitLab won't allow a merge-request to be merged into master
unless its CI checks pass.

Notice that just because CI is enabled on a project doesn't mean you are
practicing CI. To practice CI, you must regularly push changes to a feature
branch associated with a merge request, check the results of GitLab's
integration test, and integrate master into your feature branch if GitLab's
integration test fails.

## Continuous deployment/delivery

Once you know that your feature branch can be safely merged into master,
do you know that it can be safely installed and run in a known environment?
That is, is it safe to deploy? Probably not. Again, we don't want to merge
our work into master unless we know that the merged version can successfully
be deployed. And the best way to find out is to deploy the merged version.

__Continuous Deployment (CD)__ is the practice of _frequently_ deploying the
successfully integrated system into a staging or production environment.

As with CI, GitLab can be enabled to help with CD. When enabled, GitLab will
first perform CI checks, and if those pass it will try to deploy the merged
version into an existing or new environment (depending on how it is configured).
GitLab reports the results of its attempt to the merge-request. GitLab won't
allow a merge-request to be merged if it fails its CD checks.

As a bonus, when you use CD, you and other stakeholders can
interact with the deployed system allowing you to easily demo or manually
test the integrated system before merging it into master.

## GitLab setup

GitLab has built-in CI that can be enabled from the repository menu.
Click the `CI / CD` tab in GitLab and follow the [included instructions](https://gitlab.com/help/ci/quick_start/README) to enable this for your project.
