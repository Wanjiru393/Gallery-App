# Project Title

Fliq Galeria

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The Galeria project requires a prerequisite understanding of the following:

Django Framework
Python3.10
Postgres
Python virtualenv

### Set up & Installation

## Activate virtual environment
Activate virtual environment using python3.9 as default handler virtualenv -p /usr/bin/python3.9 genv && source genv/bin/activate

## Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Create the Database
- psql
- CREATE DATABASE galeria


SECRET_KEY = '<Secret_key>'
DBNAME = 'galeria'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
## Run initial Migration
python3.10 manage.py makemigrations gallery
python3.10 manage.py migrate
Run the app
python manage.py runserver


## Deployment

The application is deployed on Heroku and is live on this link:



## Built With

* Django 4.0.4 - Back end logic of the application.
* Bootstrap4 - Used for overall design and responsive site
* Pillow 9.1.1 - Used for image uploads.


## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

**Wanjiru Charity** 

## License

MIT License

Copyright (c) 2022 Wanjiru Charity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.