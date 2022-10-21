def check_type(val):
    if not val.isnumeric():
        print('Wrong value. Try again:')
        return False

    val_int = int(val)

    if val_int != 0 and val_int != 1 and val_int != 2:
        print('Wrong value. Try again:')
        return False

    return True


def check_read_line(ls, columns_count):
    if len(ls) != columns_count:
        print('Invalid number of row columns. Data reading aborted.')
        return False
    return True


def check_before_print(rows):
    if len(rows) == 0:
        print('No data to display')
        return False
    return True