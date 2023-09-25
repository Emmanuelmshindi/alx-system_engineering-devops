#!/usr/bin/python3
""" Script to export data in the csv format
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name: USER_ID.csv
"""
import requests as req
import sys
import csv
import json

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

    csv_filename = "{}.csv".format(user_id)
 
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    
        for task in resp_tasks:
            csv_writer.writerow([(task["userId"]),
                                 (resp.get("name")),
                                 (task["completed"]),
                                 (task["title"])])
