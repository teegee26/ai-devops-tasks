import requests
from requests.auth import HTTPBasicAuth
import sys

JENKINS_URL = "http://your-jenkins-url"  # e.g., http://localhost:8080
USERNAME = "your-username"
API_TOKEN = "your-api-token"

def get_jenkins_api(url, params=None):
    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(USERNAME, API_TOKEN),
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error communicating with Jenkins: {e}")
        sys.exit(1)

def list_jobs():
    url = f"{JENKINS_URL}/api/json"
    data = get_jenkins_api(url)
    jobs = data.get('jobs', [])
    print("Jobs:")
    for idx, job in enumerate(jobs, 1):
        print(f"{idx}. {job['name']}")
    return jobs

def check_latest_build_status(job_name):
    url = f"{JENKINS_URL}/job/{job_name}/api/json"
    data = get_jenkins_api(url)
    last_build = data.get('lastBuild')
    if not last_build:
        print(f"No builds found for job '{job_name}'.")
        return
    build_url = last_build['url'] + "api/json"
    build_data = get_jenkins_api(build_url)
    status = build_data.get('result')
    print(f"Latest build status for '{job_name}': {status}")

def trigger_job(job_name):
    url = f"{JENKINS_URL}/job/{job_name}/build"
    try:
        response = requests.post(
            url,
            auth=HTTPBasicAuth(USERNAME, API_TOKEN),
            timeout=10
        )
        if response.status_code in [201, 200]:
            print(f"Job '{job_name}' triggered successfully.")
        else:
            print(f"Failed to trigger job '{job_name}'. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error triggering job: {e}")

def main():
    print("Jenkins Manager")
    jobs = list_jobs()
    if not jobs:
        print("No jobs found.")
        return

    print("\nCheck status of latest builds:")
    for job in jobs:
        check_latest_build_status(job['name'])

    print("\nTrigger a job:")
    for idx, job in enumerate(jobs, 1):
        print(f"{idx}. {job['name']}")
    try:
        choice = int(input("Enter the job number to trigger (or 0 to exit): "))
        if choice == 0:
            return
        selected_job = jobs[choice - 1]['name']
        trigger_job(selected_job)
    except (ValueError, IndexError):
        print("Invalid selection.")

if __name__ == "__main__":
    main()