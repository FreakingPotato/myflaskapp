from file_handling import record_price
from file_handling import get_url
from digidirect import parseDigiDirectPrice
from georges import parseGeorgesPrice
from teds import parseTedsPrice
from camerapro import parseCameraProPrice

def scrap():
    price_dic={}
    product_dic = get_url()

    for product in product_dic.values():
        product_name = product[0]
        price_list=[]
        for x in range(1,5):
            if x == 1:
                parser = parseGeorgesPrice(product[1])
                price_list.append([parser.company, parser.parsePrice()])
            if x == 2:
                parser = parseDigiDirectPrice(product[2])
                price_list.append([parser.company, parser.parsePrice()])
            if x == 3:
                parser = parseTedsPrice(product[3])
                price_list.append([parser.company, parser.parsePrice()])
            if x == 4:
                parser = parseCameraProPrice(product[4])
                price_list.append([parser.company, parser.parsePrice()])
        price_dic[product_name] = price_list
    
    return price_dic