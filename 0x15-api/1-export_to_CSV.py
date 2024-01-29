#!/usr/bin/python3
'''
Export data in the CSV format.
'''

import csv
import requests
from sys import argv

if __name__ == '__main__':
    ui = argv[1]
    u = "https://jsonplaceholder.typicode.com/users/{}".format(ui)
    us = requests.get(url, verify=False).json()
    u = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        ui)
    td = requests.get(u, verify=False).json()
    with open("{}.csv".format(ui), 'w', newline='') as csvfile:
        tsk = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in td:
            tsk.writerow([int(ui), us.get('username'),
                                 t.get('completed'),
                                 t.get('title')])
