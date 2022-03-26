from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup


def create_faker():
    faker = []
    for i in range(20):
        ua = UserAgent()
        header = {
            'User-Agent': ua.google
        }
        url = 'https://sale.591.com.tw/?shType=list&section=9&regionid=1'

        response = requests.get(url, headers=header)
        Cookie = response.cookies.get_dict()
        response.encoding = 'utf-8'
        data = response.text

        suoP = BeautifulSoup(data, 'html.parser')

        token = suoP.find_all('meta')[11].get('content')
        header_data = {
                "User-Agent": ua.google,
                "X-CSRF-TOKEN": token,
                "Cookie": f"urlJumpIp={Cookie['urlJumpIp']};T591_TOKEN={Cookie['T591_TOKEN']};urlJumpIpByTxt={Cookie['urlJumpIpByTxt']};591_new_session={Cookie['591_new_session']}"
        }
        faker.append(header_data)
    return faker
