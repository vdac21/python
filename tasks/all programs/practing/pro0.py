import csv
import urllib.request
import json
url =("https://raw.githubusercontent.com/stockholmux/ecommerce-sample-set/master/items.json")
response=urllib.request.urlopen("https://raw.githubusercontent.com/stockholmux/ecommerce-sample-set/master/items.json")
cr = csv.reader(response)
print(cr)

