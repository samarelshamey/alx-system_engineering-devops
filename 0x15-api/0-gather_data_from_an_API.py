#!/usr/bin/python3
"""Gather data from an API"""
import requests
import re
import sys


url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            req = requests.get('{}/users/{}'.format(url, employee_id)).json()
            task_req = requests.get('{}/todos'.format(url)).json()
            employee_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == employee_id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    employee_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
