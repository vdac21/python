# SYNTAX


# Function Definition 
def myjoin(x, delim):
    output = ""
    for i in range(0, len(x)):
        output = output +x[i] + delim
    #print(output+x[len(x)-1])
    return output+x[len(x)]


#Function Call

r = myjoin(["ABC", "XYZ", "MNO"], '&')
print(r)
#"ABC-XYZ-MNO"

r = myjoin(["ABC", "XYZ", "MNO"], '-')
print(r)

r = myjoin(["ABC", "XYZ", "MNO"], '#')
print(r)
