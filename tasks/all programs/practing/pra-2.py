def myjoin(x, delim):
    output = ""
    for i in range(0, len(x)-1):
        output=output +x[i] +delim
        # print(output+x[len(x)-1])
        return output+x[len(x)-1]

r = myjoin( ["ABC", "POI", "LKJ"], '-')
print(r)
