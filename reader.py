from files import CSV_FILE_PATH
from files import JSON_FILE_PATH


read_books = open(CSV_FILE_PATH, 'r')  # r - read, w - write, a - append
read_users = open(JSON_FILE_PATH, 'r')  # open returns generator


# print(read_books.read(7)) - symbols
# print(read_books.readline()) - until \n
# print(read_books.readlines(), '\n') - return list of file
# print(read_books.read()) - all file

# read_books.close()


# with open('result.txt', 'w') as file:
#    file.write()

# with open(CSV_FILE_PATH, newline='') as f:
#     reader = csv.reader(f)
#
#     # Извлекаем заголовок
#     header = next(reader)
#
#     # Итерируемся по данным, делая из них словари
#     for row in reader:
#         print(dict(zip(header, row)))

# zip - для того, чтобы сделать словарь из двух списков (+ dict)

# with open(CSV_FILE_PATH, newline='') as f:
#     reader = csv.DictReader(f)
#
#
#     for row in reader:
#         print(row)
