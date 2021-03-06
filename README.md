# News Blogsite

### This is a python news website that uses an api to provide news to users.
#### By **Joy Machuka**

+ [Description](#Description)
+ [Setup](#Setup-Installation-Requirements)
+ [Live Site](#Live-Site)
+ [Technologies](#Technologies-and-Languages-Used)
+ [Authors Info](#Author)
+ [Licence](#Licence)

## Description

A site that helps you list and preview news articles from various sources. The news is fetched from an API and made available for you.
As a user I would like to:
* See various News sources
* Select the ones they prefer
* See the top headline articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source


## Setup-Installation-Requirements
* python3.9.12
* pip
* virtualenv

* Clone repo<br>
HTTPS: `git clone https://github.com/MachukaJoy/PasswordLocker.git`<br>
SSH: `git clone git@github.com:MachukaJoy/PasswordLocker.git`

After cloning cd into the directory and create a virtual environment name it virtual then activate it and proceed to install dependencies beloe using pip

* Creating virtual environment <br>
  python -m venv --without-pip virtual<br>
  source virtual/Scripts/activate<br>
  curl https://bootstrap.pypa.io/get-pip.py | python<br>
  source virtual/bin/activate<br>

* Necessary dependencies <br>
pip install Flask<br>
pip install Flask-Bootstrap<br>
pip install Flask-Script<br><br>

* Visit https://newsapi.org/ to get an API key then in the start.sh file replace the API key with your key as below:
  - export NEWS_API_KEY='<Your-Api-Key>'<br>
  - python3 manage.py server

* To run the application, in your terminal:
  chmod a+x start.sh
  ./start.sh

* To run the unitests run: <br>
python manage.py test

## Live-Site
## [LIVE SITE](https://news-blogsite.herokuapp.com/)

## Known Bugs
There are not any known bugs as at now. But feel free to let us know should you find any.

## Technologies-and-Languages-Used
* Python
* Visualstudio
* Flask

## Support and contact details
Should you have any issues or questions, ideas or concerns feel free to reach out to me. Also feel free to make contribution to the code and can contact me at machukajoy@gmail.com
## Author

- [Joy Machuka](https://github.com/MachukaJoy)
### Licence
[MIT LICENSE](https://github.com/MachukaJoy/PasswordLocker/blob/main/LICENSE)<br>

** <br>
Copyright (c) {2022} [Joy Machuka ](https://github.com/MachukaJoy)