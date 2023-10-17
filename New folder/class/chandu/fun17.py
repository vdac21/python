#WAF to add the middle of words in symbols

def myjoin(x,delim):
    output=""
    for i in range(0,len(x)-1):
        output=output+x[i]+delim
        #print(output+x[len(x)-1])
    return (output+x[len(x)-1])


#Function call
r=myjoin(["ABC","XYZ","MNO"],'&')
print(r)

r= myjoin(["ABC","XYZ","MNO"],'-')
print(r)
