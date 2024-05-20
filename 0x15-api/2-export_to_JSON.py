#!/usr/bin/python3
"""script to get data from api and convert it to json"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + user_id
    res = requests.get(url_to_user)
    user_name = res.json().get('username')
    url_to_task = url_to_user + '/todos'
    res = requests.get(url_to_task)
    tasks = res.json()

    dict_data = {user_id: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[user_id].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": user_name})
    """print(dict_data)"""
    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(dict_data, f)
