# wp-blog-scrapping

[![dependency](https://img.shields.io/github/pipenv/locked/dependency-version/metabolize/rq-dashboard-on-heroku/flask)](https://img.shields.io/github/pipenv/locked/dependency-version/metabolize/rq-dashboard-on-heroku/flask)
[![license-mit](https://img.shields.io/github/license/aloklearning/python-rest-api-app)](https://img.shields.io/github/license/aloklearning/python-rest-api-app)
[![githubbuild](https://img.shields.io/appveyor/build/gruntjs/grunt)](https://img.shields.io/appveyor/build/gruntjs/grunt)
[![pyversion](https://img.shields.io/pypi/pyversions/django)](https://img.shields.io/pypi/pyversions/django)

- This project helps us to scrap out all WP Blog Posts Data in an excel sheet
- It checks whether it is a valid Wordpress Website or not with the domain we provide
- Saves the `.xlsx` file on the Desktop of Cross Platform OS
- The web page is mobile friendly as well
- This is a local project, and not been hosted anywhere, however, solely for learning purpose, and to understand what `Web Scrapping` is, in this case, `Wordpress Post Scrapping` is done

## Prerequisites

- [X] You have python lates version installed in youtr box
- [X] You have installed all the files imported in the `/web-scrapping-api/blog_data.py`
- [X] `/web-scrapping-api/test.py` is just for testing puropse, not that important file

## Getting Started

- You have a little bit of understanding of Python Backend API dev, if you are looking for understanding the code
- To run the project, simply go inside the folder `/web-scrapping-api/` in your terminal and run `python3 blog_data.py`. This will run the API file on server
- You need to run the `home.html` file on your browser, simply drag and drop the file on the Web browser, and you are good to go

## Working

- Insert all the data asked in the required field.
- `Domain name` should be without `https://` and should be a valid wordpress website, for example `jacklyons.me`
- `Per Page Count` is nothing but, required as per the Wordpress blog post per page, you can put your desired number you want. `10` is the best value to be put for which WP also follows
- `Total Pages` is the total number of pages in your posts, for instance if you look at the pagination, the last page number is the total number of the pages you have. So add it accordingly

## Links

- Python Flask => [Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
- Python Docs => [Python](https://docs.python.org/3/)
- Wordpress API Docs => [WP API Handbook](https://developer.wordpress.org/rest-api/)
- Web Scrapping Definition => [Web Scrapping](https://www.scrapinghub.com/what-is-web-scraping)
- XLSX Python Docs => [Python xlsxwriter Module](https://xlsxwriter.readthedocs.io/)
