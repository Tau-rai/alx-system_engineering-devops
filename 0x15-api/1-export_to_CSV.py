#!/usr/bin/python3
"""
This module has a script that uses a REST API to gather data
and export the data in CSV format
"""

import csv
import json
import requests
import sys


def to_csv(EMPLOYEE_ID):
    """Exports employee data to csv format"""
    users_data = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}')
    todos_data = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}/todos')
    # load JSON data from the response
    data = json.loads(todos_data.text)
    user = json.loads(users_data.text)

    # specify the keys to select
    user_keys = ['username']
    data_keys = ['userId', 'completed', 'title']
    data_keys.insert(1, user_keys[0])

    # create a csv file and write data into it
    with open(f'{EMPLOYEE_ID}.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # write the header
        # writer.writerow(data_keys)

        # write the data rows
        for row in data:
            writer.writerow(
                [str(user.get(key, row.get(key, '')))
                    for key in data_keys])


if __name__ == "__main__":
    EMPLOYEE_ID = int(sys.argv[1])
    to_csv(EMPLOYEE_ID)
