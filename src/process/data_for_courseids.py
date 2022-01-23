from operator import itemgetter
import pandas as pd
import structure_class_data

df = pd.read_csv('codes.csv')

series_dict = {
    'id': [],
    'department': [],
    'class_number': [],
    'class_name': [],
    'units': []
}



for index, id in df['id'].items():
    course_info_dict = structure_class_data.get_title_data(
        f'course_data/{id}.html')
    # department, class_number, class_name, units = itemgetter(
    #     'department', 'class_number', 'class_name', 'units')(course_info_dict)
    series_dict['id'].append(id)
    for key, val in course_info_dict.items():
        series_dict[key].append(val)


all_course_info_df = pd.DataFrame(series_dict)
all_course_info_df.to_csv('course_info.csv')


