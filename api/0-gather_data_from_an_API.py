#!/usr/bin/python3
"""
This module gathers data from a REST API and displays TODO list progress for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
        employee_id = sys.argv[1]

            # Fetch user info
                user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
                    response = requests.get(user_url)
                        user_data = response.json()
                            employee_name = user_data.get('name')

                                # Fetch todos
                                    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
                                        response = requests.get(todos_url)
                                            todos_data = response.json()

                                                # Filter completed tasks
                                                    done_tasks = [task for task in todos_data if task.get('completed') is True]

                                                        print("Employee {} is done with tasks({}/{}):".format(
                                                                    employee_name, len(done_tasks), len(todos_data)))

                                                            for task in done_tasks:
                                                                        print("\t {}".format(task.get('title')))
