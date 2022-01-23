from http.client import parse_headers
from urllib import parse
import csv
import re
import requests
import bs4

all_degrees_url = 'https://catalog.fullerton.edu/content.php?catoid=70&navoid=8448'
all_degrees_res = requests.get(all_degrees_url)

degrees_soup = bs4.BeautifulSoup(all_degrees_res.text, 'html.parser')

# step 0: get all program ids


def link_to_id(link):
    href = link.get('href')
    split_query = parse.urlsplit(href).query
    querydict = parse.parse_qs(split_query)
    return querydict['poid'][0]


program_ids = list(map(link_to_id,
                       degrees_soup.select('.program-list > li > a')))

# step 1: get all urls


def degree_url(id):
    return f'https://catalog.fullerton.edu/preview_program.php?catoid=70&poid={id}&returnto=8448'


program_urls = list(map(degree_url, program_ids))
test_program = program_urls[0]

print(test_program)

# step 2: request


def get_program_info(url):
    program_res = requests.get(url)
    program_soup = bs4.BeautifulSoup(program_res.text, 'html.parser')
    return program_soup.select('.table_default')[3]


# step 3: write data
for (index, url) in enumerate(program_urls):
    print(f'remaining: {len(program_urls) - index - 1}')
    page = get_program_info(url)
    html_content = str(page.prettify())
    html_file = open(f'degree_data/{program_ids[index]}.html', 'w')
    html_file.write(html_content)
    html_file.close()
