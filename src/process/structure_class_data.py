import numpy as np
import pandas as pd
import re
import bs4

df = pd.read_csv('codes.csv')


def hello(x):
    return x + 2

# # 494128 -- math 534
# math_534 = 'test_data/494128.html'
# # 494141 -- math 599 research
# math_599 = 'test_data/494141.html'


def detect_unit_count(title_string):
    i = len(title_string) - 1
    unit_str = title_string[i]
    while(title_string[i] is not '('):
        unit_str = title_string[i] + unit_str
        i = i - 1
    return title_string[:i].strip(), unit_str


def get_title_data(class_data):
    with open(class_data, "r", encoding='utf-8') as f:
        csuf_classes_soup = bs4.BeautifulSoup(f.read(), 'html.parser')

    title_string = csuf_classes_soup.select('h1')[0].decode_contents().strip()
    classname_then_title_units = title_string.split(' - ')
    print(classname_then_title_units)
    [department, class_number] = classname_then_title_units[0].split(' ')
    if len(classname_then_title_units) == 2:
        [class_name, unit_count_group] = detect_unit_count(
            classname_then_title_units[1])
    else:
        new_title_string = ' - '.join(
            (classname_then_title_units[1], classname_then_title_units[2]))
        [class_name, unit_count_group] = detect_unit_count(new_title_string)

    pattern = re.compile('\W')
    units = list(map(lambda x: int(re.sub(pattern, '', x)),
                 unit_count_group.split('-')))
    title_data_dict = {
        'department': department,
        'class_number': class_number,
        'class_name': class_name,
        'units': units
    }
    return title_data_dict

# get_title_data(math_534)
