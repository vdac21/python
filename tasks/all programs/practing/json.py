
from bs4 import BeautifulSoup
import requests
url = "https://raw.githubusercontent.com/stockholmux/ecommerce-sample-set/master/items.json"
req = requests.get(url)
soup = BeautifulSoup(req.txt, "html.parser")
print(soup)
print(soup.prettify())



import json,urllib.request
data = urllib.request.urlopen("https://api.github.com/users?since=100").read()
output = json.loads(data)
print (output)


"""
import json
import urllib

url = 'https://api.github.com/users?since=100'
output = json.load(urllib.urlopen(url))
print(output)
"""
