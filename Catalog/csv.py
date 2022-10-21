import excep
from os.path import exists


def read_data(file_name, columns, columns_count, attributes):
    check_create_file(file_name, attributes)
    data = get_empty_data(columns)
    with open(file_name, "r", encoding="utf-8") as catalog:
        first_line = True
        for line in catalog:
            if first_line:
                # titles = get_titles(line)
                first_line = False
                continue
            cur_data = read_line(line, columns)
            if not excep.check_read_line(cur_data, columns_count):
                break
            data['rows'].append(cur_data)
        return data


def read_line(line, titles):
    line_sp = line_parser(line)
    return line_sp
    # line_data = {}
    # for i in range(0, len(titles)):
    #     line_data.setdefault(titles[i], line_sp[i])
    # return line_data


def line_parser(line):
    ls = line.split(";")
    ls = [e.replace("\n", "") for e in ls]
    return ls


def get_empty_data(columns):
    return {'columns': columns, 'rows': []}


def check_create_file(file_name, attributes):
    if not exists(file_name):
        line = ';'.join(attributes)
        with open(file_name, 'a') as file:
            file.write(line)