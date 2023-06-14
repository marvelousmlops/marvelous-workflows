# setup_env_vars

Takes the following inputs:

- **databricks_host**: Databricks host
- **databricks_token**: Databricks token

This composite action sets up the following environment variables that will be available on GitHub actions runner:
- GIT_SHA
- DATABRICKS_TOKEN
- DATABRICKS_HOST
- PROJECT_NAME

## Example usage
```
- name: Setup env vars
  id: setup_env_vars
  uses: marvelousmlops/marvelous-workflows/.github/actions/setup_env_vars@v1
    with:
      databricks_token: ${{ secrets.DATABRICKS_TOKEN }}
      databricks_host: ${{ secrets.DATABRICKS_HOST }}
```