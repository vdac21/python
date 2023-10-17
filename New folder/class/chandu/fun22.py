def read_file(filepath):
  try:
    f=open(path,'r')
    text = f.read()
    f.close()
    return text
  except:
      print(f"the file not found:{filepath}")



path="C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhus.txt"
data=read_file(path)
print(data)

