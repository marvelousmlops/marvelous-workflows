# Databricks job deployment with dbx

DBX (https://dbx.readthedocs.io/en/latest/) is a great tool that simplifies Databricks job deployment 
by taking care of uploading all dependencies (python files, whl files). You no longer need Databricks job
json definitions which can become huge and hard to read, DBX support Jinja which brings a lot of flexibility. 
Tagging, passing environment variables and python parameters - this all is also possible with DBX.

This is the main reason we chose for DBX deployment with reusable GitHub Actions workflow 
to standardize ML model deployment on Databricks.

In this repository, we provide not just reusable workflows but also reusable composite actions to 
allow for more modular setup.

## 📖 Repository structure consist of following files:
    ├── README.md                           <- The top-level README
    └── .github
        ├── workflows                       <- Reusable workflows folder
            ├── databricks_job_dbx.yml      <- Workflow for dbx deployment
            └── databricks_job_dbx.md       <- Workflow documentation
        └── actions                         <- Reusable composite actions
            ├── deploy_dbx                  <- Action for dbx deployment & documentation
            └── setup_env_vars              <- Action for setting up env vars & documentation
