#!/usr/bin/python3
"""A script that fetches info about an employee's ID using an api"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    # print("user url is: {}".format(user_url))

    # get data from api
    response = requests.get(user_url)
    # pulls the  data from api
    data = response.text
    # parses the data to JSON format
    data = json.loads(data)
    # extract user data
    name = data[0].get('name')
    # print("id is: {}".format(user_id))
    # print("name is: {}".format(name))

    # get user info about todo tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

    response = requests.get(tasks_url)

    tasks = response.text

    tasks = json.loads(tasks)

    completed = 0
    total_tasks = len(tasks)

    completed_tasks = []

    for task in tasks:

        if task.get('completed'):

            completed_tasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
