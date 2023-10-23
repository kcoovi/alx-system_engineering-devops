#!/usr/bin/python3
"""Ascript that fetches info about an employee using an api
and exports it in json format
"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    # print("user url is: {}".format(user_url))

    response = requests.get(user_url)

    data = response.text

    data = json.loads(data)

    user_name = data[0].get('username')
    # print("id is: {}".format(user_id))
    # print("username is: {}".format(user_name))

    # get user info about todo tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    # print("tasks url is: {}".format(tasks_url))

    response = requests.get(tasks_url)

    tasks = response.text

    tasks = json.loads(tasks)
    # print("JSOON LOADS IS: {}".format(tasks))

    dict_key = str(user_id)
    # print("dict_key: {}".format(dict_key))

    builder = {dict_key: []}
    for task in tasks:
        json_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": user_name
        }

        builder[dict_key].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open('{}.json'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
