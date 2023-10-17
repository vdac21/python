# Read the data from vedhu.txt and get the duplicated words the from

def read_file(filepath):
    f=open(path,'r')
    text = f.read()
    f.close()
    return text
def get_dups(tx):
    words=tx.split()
    x=[]
    y=[]
    for words in words:
        if word not in x:
            x.append(words)
        else:
            y.append(words)
    return y

path="C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt"
data=read_file(path)
print(data)

output=get_dups(data)
print(output)
