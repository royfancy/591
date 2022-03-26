from enum import Enum


class FieldName(Enum):
    field_list = [
        '房屋品牌',
        '次序',
        '案名',
        '地址',
        '價錢',
        '格局',
        '加蓋',
        '坪數',
        '樓層',
        '屋齡',
        '索引',
        '種類',
        '外觀',
        '車位',
        '網址',
        '社區',
        '段建號',
        '土地坪數',
        '朝向',
        '電話',
        '主建物',
        '附屬建物',
        '共有部分'
        ]


if __name__ == "__main__":
    print(FieldName.field_list.value)