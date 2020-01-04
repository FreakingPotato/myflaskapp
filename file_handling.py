#function record the data into a csv file named price_data.csv
import csv
import datetime

#uss csv to store the data
#current method is not extendable 
def record_price(price_dic):
    try:
        with open('price_data.csv', 'a') as csv_file:
            myFields = ['Date','Camera model','Georges','DigiDirect','Teds','CameraPro']
            csv_writer = csv.DictWriter(csv_file, fieldnames=myFields)
            if not has_header('price_data.csv'):
                csv_writer.writeheader()
            if get_date('price_data.csv') != False:
                #insert an empty line in the end
                csv_writer.writerow({'Camera model': "",'Georges': "",'DigiDirect':"",'Teds': "",'CameraPro': ""})
                csv_writer.writerow({'Date': get_date('price_data.csv')})
                for model, price in price_dic.items():
                    csv_writer.writerow({'Camera model': model,
                                        'Georges': price[0][1],
                                        'DigiDirect':price[1][1],
                                        'Teds': price[2][1],
                                        'CameraPro': price[3][1]})

    except IOError:
        print("File not accessible")

#use csv file to store every day cheapest price
def record_everyday_cheapest_price(price_dic):
    try:
        with open('everyday_cheapest_data.csv', 'a') as csv_file:
            myFields = ['date', 'Sony A7 M3', 'Sony A7 R3', 'Sony A7 R4', 'Sony A9 M1', 'Sony A9 M2', 'Sony FE35 1.8', 'Sony FE24 1.4', 'Sony FE135 1.8GM', 'Sony FE100-400GM', 'Sony FE400 2.8GM']
            csv_writer = csv.DictWriter(csv_file, myFields)

            item = []
            item_shop = []
            for x in price_dic.values():
                item_shop.append(x[0])
                item.append(x[1])

            if not has_header('everyday_cheapest_data.csv'):
                csv_writer.writeheader()

            csv_writer.writerow({'date':item_shop[0], 'Sony A7 M3':item_shop[1], 'Sony A7 R3':item_shop[2], 'Sony A7 R4':item_shop[3], 'Sony A9 M1':item_shop[4], 'Sony A9 M2':item_shop[5],
                'Sony FE35 1.8':item_shop[6], 'Sony FE24 1.4':item_shop[7], 'Sony FE135 1.8GM':item_shop[8], 'Sony FE100-400GM':item_shop[9], 'Sony FE400 2.8GM':item_shop[10]})
            csv_writer.writerow({'date':item[0], 'Sony A7 M3':item[1], 'Sony A7 R3':item[2], 'Sony A7 R4':item[3], 'Sony A9 M1':item[4], 'Sony A9 M2':item[5],
                'Sony FE35 1.8':item[6], 'Sony FE24 1.4':item[7], 'Sony FE135 1.8GM':item[8], 'Sony FE100-400GM':item[9], 'Sony FE400 2.8GM':item[10]})
    except IOError:
        print("file not accessible")

#use csv file to store current cheapest price 
def record_cheapest_price(price_dic):
    #clear the data in the csv file
    f = open("cheapest_price_data.csv", "a")
    f.truncate(0)
    f.close()
    
    try:
        with open('cheapest_price_data.csv', 'a') as csv_file:

            myFields = ['date', 'Sony A7 M3', 'Sony A7 R3', 'Sony A7 R4', 'Sony A9 M1', 'Sony A9 M2', 'Sony FE35 1.8', 'Sony FE24 1.4', 'Sony FE135 1.8GM', 'Sony FE100-400GM', 'Sony FE400 2.8GM']
            csv_writer = csv.DictWriter(csv_file, myFields)

            item = []
            item_shop = []
            for x in price_dic.values():
                item_shop.append(x[0])
                item.append(x[1])

            if not has_header('everyday_cheapest_data.csv'):
                csv_writer.writeheader()

            csv_writer.writerow({'date':item_shop[0], 'Sony A7 M3':item_shop[1], 'Sony A7 R3':item_shop[2], 'Sony A7 R4':item_shop[3], 'Sony A9 M1':item_shop[4], 'Sony A9 M2':item_shop[5],
                'Sony FE35 1.8':item_shop[6], 'Sony FE24 1.4':item_shop[7], 'Sony FE135 1.8GM':item_shop[8], 'Sony FE100-400GM':item_shop[9], 'Sony FE400 2.8GM':item_shop[10]})
            csv_writer.writerow({'date':item[0], 'Sony A7 M3':item[1], 'Sony A7 R3':item[2], 'Sony A7 R4':item[3], 'Sony A9 M1':item[4], 'Sony A9 M2':item[5],
                'Sony FE35 1.8':item[6], 'Sony FE24 1.4':item[7], 'Sony FE135 1.8GM':item[8], 'Sony FE100-400GM':item[9], 'Sony FE400 2.8GM':item[10]})
    except IOError:
        print("File not accessible")


#avoid adding redundent information based on the fact that the price won't change twice in a day
def get_date(file):
    x = datetime.datetime.now()
    date = x.strftime('%x')
    with open(file,'r') as csv_file:
        for row in csv_file:
            if date in row:
                return False

    return date

#avoid adding redundent header
def has_header(file):
    header = ['Date','Camera model','Georges','DigiDirect','Teds','CameraPro']
    with open(file,'r') as csv_file:
        for row in csv_file:
            if header[0] in row:
                return True
    return False

#get the url information from the url_data.csv
def get_url():
    try:
        price_dic={}
        with open('url_data.csv','r') as csv_file:
            csv_reader  = csv.DictReader(csv_file)
            for row in csv_reader:
                price_dic[row['Product_Number']] = [row['Product_Name'],row['Georges_url'],row['DigiDirect_url'],row['Teds_url'],row['CameraPro_url']]
            return price_dic
    except IOError:
        print("url not accessible")

