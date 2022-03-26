import asyncio
from headers.headers import Header
import requests
import time
import json
from lib.field_name import FieldName
import openpyxl
from lib.first_data import write_first_data
from lib.write_data import write_data
header_list = Header().header


async def crawl(workbook_sheet: openpyxl.Workbook().active):
    title_list = FieldName.field_list.value
    workbook_sheet.append(title_list)
    local_time = str(time.time()).replace('.', '')[:13]
    headers = header_list[0]
    url = f'https://sale.591.com.tw/home/search/list?type=2&shType=list&regionid=1&section=9&timestamp={local_time}'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    data = json.loads(response.text)
    total_data = int(data['data']['total'])
    print('共有', total_data, '筆')
    if total_data % 30 == 0:
        pages = total_data/30
    else:
        pages = total_data // 30 + 1

    detail_list = data['data']['house_list']
    data_number = 30

    task1 = asyncio.create_task(write_first_data(detail_list=detail_list, ws=workbook_sheet))

    task2 = asyncio.create_task(write_data(
        pages=pages, data_number=data_number, total_data=total_data, ws=workbook_sheet, header_list=header_list
    ))
    await task1
    await task2

    print('已下載', total_data, '筆')


if __name__ == '__main__':
    website = '591出售'
    wb = openpyxl.Workbook()
    ws = wb.active
    time_start = time.time()
    asyncio.run(crawl(workbook_sheet=ws))
    wb.save(f'{website}.xlsx')
    print(time.time() - time_start)
