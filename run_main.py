from headers.headers import Header
import requests
import time
import json
from lib.field_name import FieldName
import openpyxl
from lib.first_data import write_first_data
from lib.write_data import write_data
website = '591出售'

wb = openpyxl.Workbook()
ws = wb.active
title_list = FieldName.field_list.value
ws.append(title_list)

header_list = Header().header
local_time = str(time.time()).replace('.', '')[:13]
headers = header_list[0]
url = f'https://sale.591.com.tw/home/search/list?type=2&shType=list&regionid=1&section=9&timestamp={local_time}'
print('https://sale.591.com.tw/home/search/list?type=2&shType=list&regionid=1&section=9&timestamp=1646788557294')
print(url)
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
count = 0

count = write_first_data(detail_list=detail_list, ws=ws, count=count)

count = write_data(pages=pages, data_number=data_number, total_data=total_data, count=count, ws=ws)

print('共下載', count, '筆')
wb.save(f'{website}.xlsx')
input('輸入Enter結束.....')
