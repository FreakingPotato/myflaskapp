from flask import Flask
import bs4
import requests
from bs4 import BeautifulSoup
# Flask is a web framework. 
# It extends the capabilities of Python to allow you to create a website.

application = Flask(__name__)
application.debug = True
@application.route('/', methods=['GET'])
def hello():
 return '<p>Hello world</p>'
url = "https://www.georges.com.au/sony-a7r-mark-iv-body.html"
def parsePrice(url):
    if len(url) != 0:
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text,"lxml")
        price = soup.find_all('span',{'class':'price'})[0].text
        return price
    else:
        return 0

if __name__ == "__main__":
 application.run()