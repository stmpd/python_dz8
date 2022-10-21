import excep
import csv
import logg
import catalog


def view_welcome():
    print('Phonebook welcomes you!')
    print('\n'*1)


def input_type():
    print('What are you going to do?:')
    print('1 - read data')
    print('2 - write data')
    print('0 - exit')
    while True:
        val = input()
        if excep.check_type(val):
            return int(val)


def start():
    view_welcome()
    while True:
        type_num = input_type()
        if type_num == 0:
            break
        elif type_num == 1:
            data = catalog.gat_all_data()
            print_data(data)
        # elif type_num == 2:


def print_data(data):
    columns = data['columns']
    rows = data['rows']
    if not excep.check_before_print(rows):
        return
    columns_count = catalog.get_columns_count()
    for row in rows:
        print('-'*5)
        for column_number in range(0, columns_count):
            column_name = columns[str(column_number)]
            print("{}: {}".format(column_name, row[column_number]))
    print('-' * 5)