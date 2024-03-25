#!/usr/bin/python3
"""
This module has a script that uses a REST API to gather data
and export the data in JSON format
"""

import json
import requests


def all_to_json():
    """Exports all employees' tasks data to json format"""
    users_data = requests.get('https://jsonplaceholder.typicode.com/users')
    todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')

    # load JSON data from the response
    todos = json.loads(todos_data.text)
    users = json.loads(users_data.text)

    # create a dictionary with userId and tasks
    output = {}

    for user in users:
        USERNAME = user['username']
        USER_ID = user['id']

        # create a list of tasks for the current user
        tasks = []
        for todo in todos:
            if todo['userId'] == USER_ID:
                tasks.append({
                    "username": USERNAME,
                    "task": todo.get('title', ''),
                    "completed": todo.get('completed', False)
                })

        output[USER_ID] = tasks

    # create a json file and write data into it
    with open('todo_all_employees.json', 'w') as f:
        json.dump(output, f)


if __name__ == "__main__":
    all_to_json()
