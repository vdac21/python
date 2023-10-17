x= ['ABC','XYZ','MNO','BCG']
output = " "

for i in range(0,len(x)-1):
    output=output+x[i]
    output=output+"-"
print(output+x[len(x)-1])
