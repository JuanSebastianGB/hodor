#!/usr/bin/python3
import requests

if __name__ == '__main__':

    ID = 3393
    url = "http://158.69.76.135/level0.php"
    data = {'id': ID, 'holdthedoor': 'Submit'}
    response = requests.get(url)

    session = requests.Session()
    for i in range(1024):
        r = session.post(url, data)
