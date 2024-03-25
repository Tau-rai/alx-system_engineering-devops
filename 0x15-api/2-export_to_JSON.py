#!/usr/bin/python3
"""
This module has a script that uses a REST API to gather data
and export the data in JSON format
"""


import json
import requests
import sys


def to_json(EMPLOYEE_ID):
    """Exports employee data to JSON format"""
    users_data = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}')
    todos_data = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}/todos')
    # load JSON data from the response
    data = json.loads(todos_data.text)
    user = json.loads(users_data.text)

    # create a list of tasks
    tasks = []
    for task in data:
        tasks.append({
            "task": task.get('title', ''),
            "completed": task.get('completed', False),
            "username": user.get('username', '')
        })

    # create a dictionary with userId and tasks
    output = {EMPLOYEE_ID: tasks}

    # create a json file and write data into it
    with open(f'{EMPLOYEE_ID}.json', 'w') as f:
        json.dump(output, f)


if __name__ == "__main__":
    EMPLOYEE_ID = int(sys.argv[1])
    to_json(EMPLOYEE_ID)
