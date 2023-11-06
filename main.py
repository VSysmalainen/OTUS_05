import csv
import json
from collections import OrderedDict
from math import ceil
from files import CSV_FILE_PATH
from files import JSON_FILE_PATH


with open(CSV_FILE_PATH, 'r', newline='') as c:
    csv_data = csv.DictReader(c)
    all_books = []
    for row in csv_data:
        all_books.append(row)

with open(JSON_FILE_PATH, 'r') as j:
    json_data = json.load(j)

    part_len = ceil(len(all_books) / len(json_data))
    parts_of_books = [all_books[part_len * k:part_len * (k + 1)] for k in range(len(json_data))]

    result = []
    for i in json_data:
        users_cut_dict = {k[0]: k[1] for k in i.items() if k[0] in ('name', 'gender', 'address', 'age')}
        od = OrderedDict(users_cut_dict)
        od.move_to_end('age')
        users_cut_dict_sort = dict(od)
        users_cut_dict_sort.update({'books': parts_of_books[0]})
        parts_of_books.pop(0)
        result.append(users_cut_dict_sort)

with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)
