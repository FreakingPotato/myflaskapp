import scrapper
import datetime
import csv
from file_handling import record_price
import file_handling as fh
import time

price_dic={}

#transfer the data in csv to html
def display_price_csv():
    html = ''
    price_dic = scrapper.scrap()
    for x,y in price_dic.items():
        html += '<h2>Product: ' + x + ' :' + '</br>'
        html += '<h3>' + str(y[0]) + str(y[1]) + str(y[2]) + str(y[3])
    
    return html

#transfer the data in csv to html
def read_cheapest_price_csv():
    html = ''
    try:
        with open('cheapest_price_data.csv', 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    #present the data in table <table></table>
                    html += '<table style="width:100%">'

                    first_row = csv_reader.__next__()
                    html += '<tr>'
                    for item in first_row:
                        html += '<th>' + item + '</th>'
                    html += '</tr>'

                    second_row = csv_reader.__next__()
                    html += '<tr>'
                    for item in second_row:
                        html += '<td>' + item + '</td>'
                    html += '</tr>'

                    third_row = csv_reader.__next__()
                    html += '<tr>'
                    for item in third_row:
                        html += '<td>' + item + '</td>'
                    html += '</tr>'

                    html += '</table>'
        return html
    except IOError:
        print("File not accessible")


#record the price_dic 
# record_price(price_dic)

#find the cheapest price
def cheapest_price(price_dic):
    cheapest_dic = {}

    cheapest_dic['date'] = ['date',str(datetime.date.today())]

    for key in price_dic.keys():
        cheapest_dic[key] = ''

    for item in price_dic.items():
        cheapest_shop = [item[1][0][0]]
        cheapest_price = [item[1][0][1]]
        cheapest_list = cheapest_shop + cheapest_price
        for x in item[1]:
            if x[1] < cheapest_price[0] and x[1] != 0:
                cheapest_price = [x[1]]
                cheapest_shop = [x[0]]
                cheapest_list = cheapest_shop + cheapest_price
        cheapest_dic[item[0]]=cheapest_list
    
    return cheapest_dic
    
def camera_price_bot():
    while True:
        pd = scrapper.scrap()
        record_price(pd)
        cheapest_pd = cheapest_price(pd)
        fh.record_cheapest_price(cheapest_pd)
        fh.record_everyday_cheapest_price(cheapest_pd)
        return read_cheapest_price_csv()
