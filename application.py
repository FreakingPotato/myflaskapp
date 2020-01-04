from flask import Flask,render_template
from flask import request, redirect
from flask_apscheduler import APScheduler
import bs4
import requests
from bs4 import BeautifulSoup
from amain import read_csv

import datetime
# Flask is a web framework. 
# It extends the capabilities of Python to allow you to create a website.

# sched = BlockingScheduler()

application = Flask(__name__)
application.debug = True

# @sched.scheduled_job('interval', seconds=10)
@application.route('/', methods=['GET'])
def hello():
    return read_csv()


def current_time(text):
    print(text, str(datetime.datetime.now()))

if __name__ == "__main__":
    # scheduler = APScheduler()
    # scheduler.add_job(func=hello_world, trigger='interval', id='job', seconds=5)
    # scheduler.start()
    application.run()
    