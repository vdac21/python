"""

import sqlite3

con = sqlite3.connect("https://raw.githubusercontent.com/stockholmux/ecommerce-sample-set/master/items.json")
c = con.cursor()

c.execute("name, price, caragety")
results = c.fetchall()

for r in results:
    print(r)
"""
#get json data 

import sqlite3

try:
   con = sqlite3.connect('chinook.db')
   cur =con.cursor()
   cur.execute("select url, name, price, tag from urls")
   results = cur.fetchall
   print (results)

except Exception as e:
    print("unable to connect db: (str(e))")
