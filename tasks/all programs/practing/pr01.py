import urllib.request
import json
response=urllib.request.urlopen("https://raw.githubusercontent.com/stockholmux/ecommerce-sample-set/master/items.json")
for line in response:
    result=line.decode('utf-8')
    print(result)

