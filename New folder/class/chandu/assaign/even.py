numbers=range(0,20)
numlist=list(numbers)
newlist=[]
for ele in numlist:
    if ele % 2 == 0:
        newlist.append(ele)
print(newlist)
