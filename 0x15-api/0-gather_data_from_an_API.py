#!/usr/bin/python3
""" Script to return employee todo list"""
import requests as req
import sys

if __name__ == "__main__":

    user_id = sys.argv[2]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    url2 = (
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(user_id)
    )

    #Get completed and total tasks
    resp_tasks = req.get(url2).json()

    all_tasks = len(resp_tasks)
    done = 0

    for task in resp_tasks:
        if task["completed"]:
            done += 1

    #Get name of user
    resp = req.get(url).json()

    user_name = resp.get("name")

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, done, all_tasks))
    for task in resp_tasks:
        if task["completed"]:
            print("\t " + task["title"])
