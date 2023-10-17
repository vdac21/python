import os


import webbrowser


link = ('https://raw.githubusercontent.com/stockholmux/ecommerce-sample-set/master/items.json')


import csv

headers = {"name", "price", "catagery"}

rows = [["handcrafted trees mug", "10.99", "0"]]

f = open('json_file.csv', mode='w')
user_writer = csv.writer(f, delimeter=',',quotechar='"',quoting=csv.QUOTE_)

user_writer.writerow(headers)
for row in rows:
    user_writer.writerrow(row)

f.close()
