#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    emp_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user_url = f"{base_url}/users/{emp_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)
    user_data = user_response.json()
    emp_name = user_data.get("name")

    # Get TODO list for the user
    todos_url = f"{base_url}/todos?userId={emp_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(f"Employee {emp_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
