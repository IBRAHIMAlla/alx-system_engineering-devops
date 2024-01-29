#!/usr/bin/python3
'''
Returns information using REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        us = argv[1]
        u = "https://jsonplaceholder.typicode.com/"
        r = requests.get("{}users/{}".format(u, us))
        nm = r.json().get("name")
        if nm is not None:
            j = requests.get(
                "{}todos?userId={}".format(
                    u, us)).json()
            als = len(j)
            cp = []
            for t in j:
                if t.get("completed") is True:
                    cp.append(t)
            digit = len(cp)
            print("Employee {} is done with tasks({}/{}):"
                  .format(nm, digit, als))
            for tl in cp:
                print("\t {}".format(tl.get("title")))
