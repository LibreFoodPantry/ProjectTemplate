# Continuous Integration

Continuous Integration (CI) is the practice of frequently committing and pushing code to a project and checking that this updated code still passes tests, does not break anything, and can successfuly merge with existing code. This is helped by tools on GitHub and GitLab that automatically perform testing when code is pushed to a repository and not allowing commits to be merged if the tests fail. This ensures that the master branch always contains working code that functions as intended.

For a more in-depth look at CI see [GitHub's video about CI](https://youtu.be/xSv_m3KhUO8)

## GitHub setup:
[GitHub's marketplace](https://github.com/marketplace/category/continuous-integration) has many different apps that add CI functionality to a repository. To enable CI for a project, add a CI app from the GitHub marketplace to your account and enable it for your repository and follow the setup instructions.

## GitLab setup:
GitLab has built-in CI that can be enabled from the repository menu.
Click the `CI / CD` tab in GitLab and follow the [included instructions](https://gitlab.com/help/ci/quick_start/README) to enable this for your project.