#!/usr/bin/python3
'''
Export data in the JSON format
'''

import json
import requests
from sys import argv


if __name__ == "__main__":

    import json
    import requests
    import sys

    uss = requests.get("https://jsonplaceholder.typicode.com/users")
    uss = uss.json()
    td = requests.get('https://jsonplaceholder.typicode.com/todos')
    td = td.json()
    tdAll = {}

    for us in uss:
        tl = []
        for t in td:
            if t.get('userId') == us.get('id'):
                tDict = {"username": us.get('username'),
                            "task": t.get('title'),
                            "completed": t.get('completed')}
                tl.append(tDict)
        tdAll[us.get('id')] = tl

    with open('todo_all_employees.json', mode='w') as m:
        json.dump(tdAll, m)


