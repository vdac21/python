# SYNTAX


# Function Defination
def myjoin(x):
    output = ""
    for i in range(0, len(x)-1):
        output = output + x[i] + "-"
    print(output+x[len(x)-1])


# Function call

myjoin(["ABC","XYZ","MNO"])

