
import time
import pandas as pd
import requests
import bs4


def class_page(id):
    return f'https://catalog.fullerton.edu/preview_course_nopop.php?catoid=70&coid={id}'


# Get all the course codes and turn them into URLs
df = pd.read_csv('codes.csv')
df['urls'] = df['id'].apply(class_page)


def get_info_from_page(url):
    """Get the info from an individual URL"""
    first_res = requests.get(url)
    first_soup = bs4.BeautifulSoup(first_res.text, 'html.parser')
    all_course_info = first_soup.select('#course_preview_title')[0].parent
    return all_course_info


# The scraper loop for every single URL
# Outputs html file {course code}.html with relevant info
# Set to scrape in chunks of 200 every 3 minutes
# So as to not overload the servers
for index, row in df.iterrows():
    print(f'remaining: {df.count() - index - 1}')
    children = get_info_from_page(row['urls'])
    html_content = str(children.prettify())
    html_file = open(f'course_data/{row["id"]}.html', 'w')
    html_file.write(html_content)
    html_file.close()
    if (index != 0 and index % 200 == 0):
        print('waiting for next iteration...')
        time.sleep(180)
