# Cobining all related togetthe in a single file is called module
# Library File 
def read_file(path):
    f = open(path, 'r')
    text = f.read()
    f.close()
    return text

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_file(path, data):
    f = open(path, 'a')
    f.write(data)
    f.close()


  
