# Deploy dbx composite action

Takes the following inputs:

- **workspace-dir**: Workspace directory on Databricks, needed for dbx configuration
- **artifact-location**: Artifact location on Databricks, needed for dbx configuration
- **deployment-file**: dbx deployment file
- **run-job-now**: if yes, directly runs Databricks job

This composite action consists of following steps:
- setup python
- checkout repository
- install dependencies: dbx, databricks-cli
- configure dbx project
- get Databricks job name from dbx deployment file
- deploy dbx & launch Databricks job if run-job-now input is "yes"

##Prerequisites:
This action requires DATABRICKS_TOKEN and DATABRICKS_HOST environment variables.

## Example usage
```
- name: Deploy dbx
  id: deploy_dbx
  uses: marvelousmlops/marvelous-workflows/.github/actions/deploy_dbx@v1
    with:
      workspace-dir: "/Shared/amazon-reviews-databricks"
      artifact-location: "dbfs:/Shared/amazon-reviews-databricks"
      deployment-file: "conf/dbx_deployment.j2"
      run-job-now: "yes"
```

