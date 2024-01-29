#!/usr/bin/python3
'''
Export data in the CSV format.
'''

import csv
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

    tl = 0

    for d in jr:
        if d['completed']:
            tl += 1

    fCSV = ie + '.csv'

    with open(fCSV, "w", newline='') as csvf:
        wt = csv.writer(csvf, delimiter=',', quoting=csv.QUOTE_ALL)
        for m in jr:
            wt.writerow([ie, us, m.get('completed'), m.get('title')])
