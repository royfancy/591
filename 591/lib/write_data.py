import json
import random
import time
import openpyxl
import requests
from lib.first_data import write_first_data
from headers.headers import Header


def write_data(pages: int, data_number: int, total_data: int, count: int, ws: openpyxl.Workbook().active):
    header_list = Header().header
    for page in range(pages - 1):
        time.sleep(random.random() / 5 + 0.03)
        if page % 15 == 0:
            print('載入中', end='')
            for i in range(5):
                print('.', end='', flush=True)
                time.sleep(random.random())
            print()
        local_time = str(time.time()).replace('.', '')[:13]
        headers = header_list[random.randrange(20)]
        url = f'https://sale.591.com.tw/home/search/list?type=2&shType=list&regionid=1&section=9&firstRow={data_number}&totalRows={total_data}&timestamp={local_time} '
        data_number += 30
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        try:
            data = json.loads(response.text)
        except Exception as e:

            print(response)
            print(e)
            print(page)
            print(pages)
            print(headers)
            with open('error_agen.text', 'a') as f:
                f.write(str(headers) + '\n')
            time.sleep(10)
            continue

        detail_list = data['data']['house_list']
        count = write_first_data(detail_list=detail_list, ws=ws, count=count)
    return count
