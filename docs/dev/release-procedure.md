# Release Procedure


## Standard Release Procedure

1. Test HEAD of master thoroughly.
2. Review and update the change log.
3. Determine the new version number by determining if there was a breaking change since the last release. If there was, it's a major bump; if not, it's a minor bump.
4. Update all version numbers in source files and commit (a.k.a. bump version).
5. Tag with `<major>.<minor>.<patch>`.
6. Branch with `release/<major>.<minor>`.
7. Push the new branch and tags.

Consider using a tool to automate this process: see
[Tooling for Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/#tooling-for-conventional-commits)


## Patch Release Procedure

A patch fixes a bug in an existing release.
This is how to release a patch.

1. Fix the bug in master (not in the release branch).
2. Cherry-pick the commit(s) into the release branch.
3. Test release branch thoroughly.
4. Update change log.
5. Bump version and tag on the release branch.
6. Push release branch and tags.
