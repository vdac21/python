# combining all related together in a single file is called
# Library file
def read_file(path):
    f = open(path, 'r')
    text = f.read()
    f.close()
    return text
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_file(path,data):
    f = open(path, 's')
    f.write(data)
    f.close()
