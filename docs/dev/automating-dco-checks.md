# Automating DCO (Developer Certificate of Origin) checks

Each commit in a merge-request must contain a `Signed-off-by` line before
it can be merged. Reviewers must check for these when review a merge-request.

On GitHub, one may automate these checks by enabling
[Probot's DCO bot](https://probot.github.io/apps/dco/).
Then, under `Settings` and `Branches`, you must protect `master` and turn on
`Require status checks to pass before merging` and then select `DCO`.
