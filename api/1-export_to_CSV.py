s script fetches tasks for a given employee ID from a REST API and
exports them into a CSV file.

CSV format:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

Usage:
    ./1-export_to_CSV.py <employee_id>
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    emp_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_response = requests.get(f"{base_url}/users/{emp_id}")
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    user = user_response.json()
    username = user.get("username")

    # Get TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={emp_id}")
    todos = todos_response.json()

    # Write to CSV file
    filename = f"{emp_id}.csv"
    with open(filename, mode="w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])

