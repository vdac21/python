import shutil
from os import path
def main():
    if path.exists("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\TEST"):
        src = path.realpath("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\TEST");
    root_dir,tail=path.split(src)
    shutil.make_archive("test archive","zip",root_dir)
if __name__=="__main__":
    main()
