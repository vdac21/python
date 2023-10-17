#combine all the charcters from the given sentence with respective indices are divisable by 5 and ignore the space in output


sen="Winners are not those who never fail but those who never quit"

res= " "


for i in range(0,len(sen)):
    if i%5==0:
        if sen[i]!=' ':
           res=res+sen[i]
print(res)
