from flask import Flask
import bs4
import requests
from bs4 import BeautifulSoup
from amain import display_price, main
# Flask is a web framework. 
# It extends the capabilities of Python to allow you to create a website.

# from apscheduler.schedulers.blocking import BlockingScheduler
# sched = BlockingScheduler()

application = Flask(__name__)
application.debug = True

# @sched.scheduled_job('interval', seconds=10)
@application.route('/', methods=['GET'])
def hello():
    # message = 'Hello my Dear, please find the price of my Xmas Gift below '
    # print(message)
    main()
    return display_price()

if __name__ == "__main__":
 application.run()