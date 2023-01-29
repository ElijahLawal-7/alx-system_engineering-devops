#!/usr/bin/python3
""" a script that converts data to json """


import json
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(userId)
            )

    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    todoUser = {}
    taskList = []

    for task in todos.json():
        if task.get('userId') == int(userId):
            taskDict = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.json().get('username')
                    }
            taskList.append(taskDict)
        todoUser[userId] = taskList

    filename = userId + '.json'

    with open(filename, mode="w") as f:
        json.dump(todoUser, f)
