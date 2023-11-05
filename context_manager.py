from files import CSV_FILE_PATH

with open(CSV_FILE_PATH, 'r') as file:
    print(file.read())
    # No need to call close method

# print('\n', 20 * '=', '\n')
#
# with open(CSV_FILE_PATH, 'r') as file:
#     for line in file.readlines():
#         print(line, end='')
