# CSU Fullerton Scraper

Scrapes data from the CSU Fullerton site and stores the main content in HTML files associated with each course/degree ID.

Pages scraped:

* [Course Descriptions](https://catalog.fullerton.edu/content.php?catoid=61&navoid=7399)
* [Degree Programs](https://catalog.fullerton.edu/content.php?catoid=61&navoid=7397).

Assumes the use of `conda` or `mamba` to create an environment based on `requirements.txt`.

## To get class info:

### WARNING: don't run get_class_info_scraper will go through 3950 or so requests as-is.

1. `python get_codes_scraper.py` to get all class codes in a csv
2. `python get_class_info_scraper.py` to go through every single class page and get the descriptions into html files

## To get degree program info:

Run `python get_degree_program_info.py`.

More coming soon.