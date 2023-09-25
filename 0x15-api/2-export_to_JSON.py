#!/usr/bin/python3
""" Script to export data in the csv format
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name: USER_ID.csv
"""
import requests as req
import sys
import csv
import json
from collections import OrderedDict

if __name__ == "__main__":

    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    url2 = (
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(user_id)
    )

    #Get completed status and titles
    resp_tasks = req.get(url2).json()

    #Get name of user
    resp = req.get(url).json()

    json_filename = "{}.json".format(user_id)

    json_data = OrderedDict()
 
    json_data[user_id] = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": resp.get("username")
        }
        for task in resp_tasks
    ]

    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)
