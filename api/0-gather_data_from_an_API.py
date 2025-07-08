mport requests
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee info
    user_resp = requests.get(f"{base_url}/users/{employee_id}")
    if user_resp.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    employee = user_resp.json()
    employee_name = employee.get('name')

    # Fetch todos for the employee
    todos_resp = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    if todos_resp.status_code != 200:
        print(f"Error: Could not retrieve TODOs for employee {employee_id}.")
        return

    todos = todos_resp.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]

    # Print progress
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer.")
        sys.exit(1)

    fetch_employee_todo_progress(emp_id)
