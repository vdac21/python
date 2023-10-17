

def read_file(filepath):
    try:
        f = open(filepath, 'r')
        data = f.read()
        f.close()
        return data
    except:
        print(f"The file not found : {filepath}")


#path = 'C:\\Users\\91998\\Desktop\\rm2022H2\\zenpython.log'

path = input("Enter File path : ")
data = read_file(path)
print(data)
