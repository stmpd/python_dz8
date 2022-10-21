import csv

columns = {'0': 'ID', '1': 'Surname', '2': 'Name', '3': 'PhoneNumber', '4': 'Description'}
columns_count = 5
file_name = "catalog.csv"


def get_columns():
    global columns
    return columns


def get_attributes():
    global columns
    global columns_count
    ls = []
    for i in range(0, columns_count):
        ls.append(columns[str(i)])
    # ls.remove('ID')
    return ls


def gat_all_data():
    global columns
    global file_name
    global columns_count
    attributes = get_attributes()
    data = csv.read_data(file_name, columns, columns_count, attributes)
    return data


def get_columns_count():
    global columns_count
    return columns_count