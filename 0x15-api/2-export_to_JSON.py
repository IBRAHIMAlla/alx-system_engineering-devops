#!/usr/bin/python3
'''
Export data in the JSON format.
'''

import json
import requests
from sys import argv


if __name__ == "__main__":

    se = requests.Session()

    ie = argv[1]
    u = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(ie)
    nu = 'https://jsonplaceholder.typicode.com/users/{}'.format(ie)

    em = se.get(u)
    emName = se.get(nu)

    jr = em.json()
    us = emName.json()['username']

    tl = []
    upu = {}

    for Emp in jr:
        tl.append(
            {
                "task": Emp.get('title'),
                "completed": Emp.get('completed'),
                "username": us,
            })
    upu[ie] = tl

    fj = ie + ".json"
    with open(fj, 'w') as m:
        json.dump(upu, m)
