from flask import Flask
import bs4
import requests
from bs4 import BeautifulSoup
from amain import main
# Flask is a web framework. 
# It extends the capabilities of Python to allow you to create a website.

application = Flask(__name__)
application.debug = True
@application.route('/', methods=['GET'])
def hello():
    message = 'Hello my Dear, please find the price of my Xmas Gift below '
    print(message)
    return main()


# def parsePrice(url):
#     if len(url) != 0:
#         r = requests.get(url)
#         soup = bs4.BeautifulSoup(r.text,"html")
#         price = soup.find_all('span',{'class':'price'})[0].text
#         return price
#     else:
#         return 0

if __name__ == "__main__":
 application.run()