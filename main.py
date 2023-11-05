import csv
import json
from files import CSV_FILE_PATH
from files import JSON_FILE_PATH
from collections import OrderedDict
from math import ceil


with open(CSV_FILE_PATH, 'r', newline='') as c:
    csv_data = csv.DictReader(c)
    all_books = []
    for row in csv_data:
        all_books.append(row)

with open(JSON_FILE_PATH, 'r') as j:
    json_data = json.load(j)

    part_len = ceil(len(all_books) / len(json_data))
    parts_of_books = [all_books[part_len * k:part_len * (k + 1)] for k in range(len(json_data))]

    s = []
    for i in json_data:
        d = {k[0]: k[1] for k in i.items() if k[0] in ('name', 'gender', 'address', 'age')}
        od = OrderedDict(d)
        od.move_to_end('age')
        b = dict(od)
        b.update({'books': parts_of_books[0]})
        parts_of_books.pop(0)
        s.append(b)

with open('result.json', 'w') as file:
    json.dump(s, file, indent=4)
