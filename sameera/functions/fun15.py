def myjoin(x,delim):
    output=" "
    for i in range(0,len(x)-1):
        output=output+x[i]+delim
    return output+x[len(x)-1]
r=myjoin(["ABC","XYZ","MNO"],'&')
print(r)
r1=myjoin(["ABC","XYZ","MNO"],'$')
print(r1)
        
    
