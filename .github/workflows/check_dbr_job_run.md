# check_dbr_job_run.yml

This workflow can be used as a template for waiting databricks training job and checking the status.
At the same time, it is meant as a reusable workflow.

## What it does
The workflows runs the following steps using composite actions form gso-ml-toolkit one after another:
- **echo inputs**: this is important since there is no way to check inputs of the workflow run
when it is triggered on workflow dispatch afterwards
- **setup_env_vars**: see .github/actions/setup_env_vars.md
- **check_dbr_job_run**: Checks dbr job run by running pythin script


### Required inputs

#### run_id
Databricks run_id for train job to generate model artifact.

#### toolkit_ref
gso-ml-toolkit reference.


### Example of usage:

```
name: Your-Project-Name
on: [push]
jobs:
  YOUR-JOB-NAME-HERE:
    uses: RoyalAholdDelhaize/gso-ml-toolkit/.github/workflows/check_dbr_job_run.yml@COMMIT_HASH_YOU_WANT_TO_USE
    with:
      run_id: <run id>
      toolkit_ref: "master"
    secrets: inherit
```
