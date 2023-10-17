#  Read the data from zenof_python.log and get the duplicated words the from 


def read_file(filepath):
    f = open(path, 'r')  
    text = f.read()
    f.close()
    return text

def get_dups(tx):
    words = tx.split()
    x = []
    y = []
    for word in words:
        if word not in x:
            x.append(word)
        else:
            y.append(word)
    return y

    
path = 'C:\\Users\\91998\\Desktop\\rm2022H2\\zenpython.log'
data = read_file(path)
#print(data)


output = get_dups(data)
print(output)
