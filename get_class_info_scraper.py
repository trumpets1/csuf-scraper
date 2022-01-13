
import pandas as pd
import numpy as np
import requests
import bs4


def class_page(code):
    return f'https://catalog.fullerton.edu/preview_course_nopop.php?catoid=70&coid={code}'


df = pd.read_csv('codes.csv')
df['urls'] = df['courseids'].apply(class_page)


def get_info_from_page(url):
    first_res = requests.get(url)
    first_soup = bs4.BeautifulSoup(first_res.text, 'html.parser')
    all_course_info = first_soup.select('#course_preview_title')[0].parent
    return all_course_info


test_url = df['urls'][0]
children = list(filter(lambda child: child.name != 'br',
                get_info_from_page(test_url).contents))

new_children = np.array(children, dtype='object')

def is_h1(x): return x.name == 'h1'

is_h1_vec = np.vectorize(is_h1)
bool_arr = is_h1_vec(new_children)
print(new_children[bool_arr])
