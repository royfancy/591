import re
import openpyxl


def find_chinese(title):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', title)
    return chinese


def write_first_data(detail_list: list, count: int, ws: openpyxl.Workbook().active):
    for detail_data in detail_list:
        count += 1
        title_remix = detail_data['title'].replace('舘', '館').replace('岡', '崗')
        title = find_chinese(title_remix)
        address = detail_data['region_name'] + detail_data['section_name'] + detail_data['address']
        for i in range(10):
            address = address.split(f'{i}')[0]
        price = detail_data['price']
        pattern = detail_data['room']
        add_building = ''
        area = detail_data['area']
        floor_data = detail_data['floor'].split('/')
        floor_final = floor_data[-1].replace('F', '')
        floor_first = floor_data[0].replace('F', '').replace('/', '=').replace('整棟', '1').replace('頂樓加蓋', floor_final)

        if detail_data['shape_name'] == '透天厝' or detail_data['shape_name'] == '別墅':
            floor = detail_data['floor'].replace('F', '').replace('/', '-').replace('整棟', '1') + '=' + floor_final
        elif floor_final == '':
            floor = ''
        else:
            floor = floor_first + '=' + floor_final
        age = detail_data['houseage']
        type_name = detail_data['shape_name']
        if '含車位' in detail_data['tag']:
            parking = '有'
        else:
            parking = '沒有'
        url_name = 'https://newhouse.591.com.tw//' + f'home/house/detail/{detail_data["type"]}/{detail_data["houseid"]}.html'
        data_write = [
            '591出售',
            '',
            title,
            address,
            price,
            pattern,
            add_building,
            area,
            floor,
            age,
            '',
            type_name,
            '',
            parking,
            url_name,
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ]
        print('以下載', count, data_write[2])
        try:
            ws.append(data_write)
        except:
            print()
            data_write[2] = ''
            ws.append(data_write)
    return count
