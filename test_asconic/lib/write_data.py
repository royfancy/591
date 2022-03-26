import asyncio
import json
import random
import time
import openpyxl
import requests
from lib.first_data import write_first_data


async def response_get(url: str, headers: dict):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response


async def asonic_write_data(page: int, pages: int, data_number: int, total_data: int, ws: openpyxl.Workbook().active, header_list: list):
    print(page, '**'*100)
    if page % 15 == 0:
        print('載入中', end='')
        for i in range(5):
            print('.', end='', flush=True)
            time.sleep(random.random())
        print()
    local_time = str(time.time()).replace('.', '')[:13]
    headers = header_list[random.randrange(20)]
    url = f'https://sale.591.com.tw/home/search/list?type=2&shType=list&regionid=1&section=9&firstRow={data_number}&totalRows={total_data}&timestamp={local_time} '
    response = await response_get(url=url, headers=headers)
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
        return

    detail_list = data['data']['house_list']
    await write_first_data(detail_list=detail_list, ws=ws)


async def write_data(
        pages: int, data_number: int, total_data: int, ws: openpyxl.Workbook().active, header_list: list
):
    tasks = [asonic_write_data(pages=pages, page=page, data_number=data_number*page, header_list=header_list, total_data=total_data, ws=ws) for page in range(pages - 1)]
    await asyncio.gather(*tasks, return_exceptions=True)
