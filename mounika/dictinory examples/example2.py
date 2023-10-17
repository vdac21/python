#merge two python dictionaries into one

dict1={'ten': 10, 'twenty': 20, 'thirty': 30}
dict2={'fourty': 40, 'fifty': 50, 'sixty': 60}
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)

import json
x={"name":"jhon",
"age":30,
"job":True,
"Education":False,
"Id section":(1,2,3),
"Teaching":None,
"students":[
    {"name":"Alex","Add":"MYC"},
    {"name":"new","Add":"UK"}]}
print(json.dumps(x))
