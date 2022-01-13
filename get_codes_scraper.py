import csv
import re
import requests
import bs4

first_res = requests.get(
    'https://catalog.fullerton.edu/content.php?catoid=70&navoid=8450')

# step 0: see how many pages
csuf_classes_soup = bs4.BeautifulSoup(first_res.text, 'html.parser')
links = csuf_classes_soup.select('.table_default tr a')
real_links = list(filter(lambda x: x is not None, map(
    lambda a: a.get('aria-label'), links)))

# what I really wanted: returns the last page to go to
upper_limit = int(real_links[-1].split(' ')[1])

# step 1: gather the urls


def page_number(x):
    return f'https://catalog.fullerton.edu/content.php?catoid=70&catoid=70&navoid=8450&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D={x}#acalog_template_course_filter'


urls_to_visit = [page_number(i) for i in range(1, upper_limit + 1)]

# step 2: extract course ids from onclick methods on the page


def get_course_ids_from_page(res):
    csuf_classes_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    classes = csuf_classes_soup.select('.width > a')
    onclicks = list(map(lambda class_link: class_link.get('onclick'), classes))
    course_codes = list(map(lambda t: re.sub(
        "[^0-9]", "", t.split(',')[1].strip()), onclicks))
    return course_codes


def get_courses_at_url(url):
    res = requests.get(url)
    return get_course_ids_from_page(res)


# step 3: do this for every page in the catalog
course_codes = list(map(get_courses_at_url, urls_to_visit))


# step 4: flatten and write all the course codes to csv
flat_course_codes = list(map(lambda code: [code], [
    item for sublist in course_codes for item in sublist]))

with open('codes.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    header = ['courseids']
    writer.writerow(header)
    writer.writerows(flat_course_codes)
