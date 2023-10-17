

def read_file(filepath):
    try:
        f = open(filepath, 'r')
        data = f.read()
        f.close()
        return data
    except:
        print(f"The file not found : {filepath}")


path = "C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\New folder\\class\\fun_example\\txt.log"

#path = input("Enter File path : ")
data = read_file(path)
print(data)
