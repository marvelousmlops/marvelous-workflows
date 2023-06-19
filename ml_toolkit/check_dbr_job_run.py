import time
import requests
import argparse
import os


def databricks_get_api(endpoint, json: dict = None):
    domain = os.getenv("DATABRICKS_HOST")
    token = os.getenv("DATABRICKS_TOKEN")
    print(f"{domain}/api/{endpoint}")

    if json:
        response = requests.get(
            f"{domain}/api/{endpoint}",
            headers={"Authorization": f"Bearer {token}"},
            json=json,
        )
    else:
        response = requests.get(
            f"{domain}/api/{endpoint}",
            headers={"Authorization": f"Bearer {token}"},
        )
    return response


def get_run_status(run_id):
    """Retrives run status for a given Databricks run

    Args:
        run_id (str): Unique identifier for a specific jon rub

    Returns:
        str: The status of the job
    """
    response = databricks_get_api(endpoint=f"2.0/jobs/runs/get?run_id={run_id}")

    if response.status_code == 200:
        return response.json()["state"]
    else:
        print(response.json()["message"])


def get_arguments():
    parser = argparse.ArgumentParser(
        description="databricks job json file parser and adjustment"
    )
    parser.add_argument(
        "--run_id", metavar="run_id", type=str, default="", help="Databricks run id"
    )

    args = parser.parse_args()
    return args.run_id


if __name__ == "__main__":
    for env_var in ["DATABRICKS_HOST", "DATABRICKS_TOKEN"]:
        if env_var not in os.environ:
            raise EnvironmentError(
                f"Must provide value for {env_var} environment variable"
            )

    run_id = get_arguments()
    state_dict = get_run_status(run_id=run_id)
    sleep_time = "60"

    while (
        state_dict["life_cycle_state"] == "RUNNING"
        or state_dict["life_cycle_state"] == "PENDING"
    ):
        print(
            f"Databricks job status is {state_dict['life_cycle_state']}, sleeping %s seconds"
            % str(sleep_time)
        )
        time.sleep(sleep_time)
        state_dict = get_run_status(run_id=run_id)
    else:
        if state_dict["life_cycle_state"] == "INTERNAL_ERROR":
            RuntimeError("Given databricks run failed.")
            if (
                state_dict["life_cycle_state"] == "TERMINATED"
                and state_dict["result_state"] == "SUCCESS"
            ):
                print(state_dict["result_state"])
