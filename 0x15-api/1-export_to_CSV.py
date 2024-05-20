#!/usr/bin/python3
"""export api to cvs"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(user_url)
    user_name = res.json().get('username')
    task = user_url + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed_tasks = task.get('completed')
            task_title = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed_tasks, task_title))
