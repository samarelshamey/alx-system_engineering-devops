#!/usr/bin/python3
"""script to fetch rest apo for employee todo list"""
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    req = requests.get(url)
    users = req.json()

    users_dict = {}
    for user in users:
        USER_ID = user.get('id')
        USER_NAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url = url + '/todos/'
        req = requests.get(url)

        tasks = req.json()
        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USER_NAME
            })
            """A little Something"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
