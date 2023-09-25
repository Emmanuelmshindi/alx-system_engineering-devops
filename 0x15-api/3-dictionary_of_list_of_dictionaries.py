#!/usr/bin/python3
""" Script to export data in the csv format
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name: USER_ID.csv
"""
from collections import OrderedDict
import csv
import json
import requests as req
import sys

if __name__ == "__main__":

    response = req.get("https://jsonplaceholder.typicode.com/users").json()
    user_ids = [str(user['id']) for user in response]

    todo_all_employees = OrderedDict()

    for user_id in user_ids:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        url2 = (
            "https://jsonplaceholder.typicode.com/users/{}/todos"
            .format(user_id)
        )

        # Get completed status and titles
        resp_tasks = req.get(url2).json()

        # Get name of user
        resp = req.get(url).json()

        json_data = OrderedDict()

        json_data[user_id] = [
            {
                "username": resp.get("username"),
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in resp_tasks
        ]

        todo_all_employees.update(json_data)

    json_filename = "todo_all_employees.json"

    with open(json_filename, 'w') as jsonfile:
        json.dump(todo_all_employees, jsonfile)
