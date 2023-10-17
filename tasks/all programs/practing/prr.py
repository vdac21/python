import sqlite3

con = sqlite3.connect("https://raw.githubusercontent.com/stockholmux/ecommerce-sample-set/master/items.json")
c = con.cursor()

c.execute("name, price, caragety")
results = c.fetchall()

for r in results:
    print(r)
