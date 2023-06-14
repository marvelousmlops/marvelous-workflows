# databricks_job_dbx

Databricks_job_dbx.yml is a reusable workflow that consists of the following steps:

- **echo workflow inputs**: this step is important to be able to find out when the workflow exactly 
ran and what inputs it had at a later stage

- **generate token**: this step generates a GitHub token from Github App that has read permissions
for all repositories within organization

- **setup GIT_TOKEN** as environment variable

- **Get composite run steps repository**. This step is extremely important.

Checkout marvelous-workflows repository using GIT_TOKEN.

We use composite actions which are defined in the same repository as GitHub Actions workflow 
and want to reference composite actions, we can not use relative path. When the workflow is
called from another repository, for example, marvelousmlops/amazon-reviews-databricks, it would
then look for action defined in amazon-reviews-databricks repository. 

We could then just reference our actions as marvelousmlops/deploy_dbx@v1 and marvelousmlops/setup_env_vars@v1,
but this approach would have some limitations: every time the workflow is updated and new git tag is created,
we would also need update action version in the workflow, which would lead us to a loop situation.

If we just reference it as @master/ @develop, it will cause conflicts: if someone chooses to stay on 
version v1 of the workflow and actions in the corresponding branch get updated, workflow may start doing
unexpected things. We want all versions to be stable.

It leaves us with the following solution: checking out the workflows repository with a certain reference.
In that way we can ensure that version v1 of the workflow will always stay the same

- **Setup environment variables**
This step will setup environment variables: GIT_SHA, DATABRICKS_TOKEN, DATABRICKS_HOST, PROJECT_NAME.
PROJECT_NAME is the same as repository name, GIT_SHA is git commit hash, 
values for DATABRICKS_TOKEN and DATABRICKS_HOST are taken from the values of corresponding secrets.

In this article https://medium.com/marvelous-mlops/going-serverless-with-databricks-part-2-feccb19162fe we explain 
how to setup a long living DATABRICKS_TOKEN for SPN for automation. 

- ** Deploy dbx**
Deploys job on Databricks using dbx as described in deploy_dbx action documentation