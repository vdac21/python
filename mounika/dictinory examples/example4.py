#Initialize dictionary with default values

employees=['kelly','Emma']
defaults={"designation": 'developer',"salary":80000}

res=dict.fromkeys(employees,defaults)
print(res)



print(res["kelly"])
