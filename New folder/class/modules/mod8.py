#  Get the score of Manohar  from the file data.txt
import json


f = open('vedhu.txt', 'r')
data = f.read()
f.close()

#print(data["Manohar"])
print(data)
print(type(data))
print("------------------------------------------")
resp = json.loads(data)
print(resp)
print(type(resp))
print(resp["Manohar"])
# use slicing  - Mahesh 

# data["Manohar"] - Pravallik K
