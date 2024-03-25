#!/usr/bin/python3
"""
This module has a script that uses a REST API to gather data
"""

import json
import requests
import sys


def progress_list(EMPLOYEE_ID):
    """Checks is employee's todos progress"""
    users_data = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}')
    user = users_data.json()
    todos_data = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}/todos')
    tasks = todos_data.json()

    EMPLOYEE_NAME = user['name'] if user else 'Unknown'

    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([todo for todo in tasks if todo['completed']])

    fstring = "Employee {} is done with ({}/{})".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
    print(fstring)
    for task in tasks:
        if task['completed']:
            TASK_TITLE = task['title']
            print(f"\t {TASK_TITLE}")


if __name__ == "__main__":
    EMPLOYEE_ID = int(sys.argv[1])
    progress_list(EMPLOYEE_ID)
