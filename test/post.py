#!  /usr/bin/env python

from __future__ import print_function

import json
import requests
import sys

from requests.auth import HTTPBasicAuth

AUTH_USER       = 'roma'
AUTH_PASSWORD   = 'romaroma'
HEADERS         = { 'content-type' : 'application/json' }
URL_API         = 'http://localhost:8000/api/'

r = requests.get(URL_API + 'author/')

print(r.status_code)

response = json.loads(r.content)

for k, v in sorted(response.items()):
    if k in ('results'):
        print('{:<12s} ='.format(k))
        for i in v:
            for kk, vv in sorted(i.items()):
                print('{:<4s}{:<12s} = {}'.format(' ', kk, vv))
            print()
    else:
        print('{:<12s} = {}'.format(k, v))

test_author = \
    {
    'first_name'    : 'Jon',
    'last_name'     : 'Roma',
    }

r = requests.post \
    (URL_API + 'author/', 
     auth=HTTPBasicAuth(AUTH_USER, AUTH_PASSWORD),
     headers=HEADERS,
     data=json.dumps(test_author))

print(r.status_code)

response = json.loads(r.content)

for k, v in sorted(response.items()):
    print('{:<12s} = {}'.format(k, v))
