
import os
import shutil
import os.path, time

ROOT="C:\\Program Files\\Microsoft SQL Server"

def get_all_filepaths(root1):
    file_paths = []
    files = []
    for root, dirs, filenames in os.walk(P1):
        for filename in filenames:
            filename=os.path.join(root, filename)
            file_paths.append(filename)
            for file_path in file_paths:
                if file_path.endswith(".dll") or (".exe"):
                    files.append(file_path)
     return files
R=get_all_filepaths(ROOT)
print(f"ALL file_paths that endswith .EXE and .DLL : {R}")

def maxfile(root2):
    file_paths = []
    files =[]
    dll_files=[]
    exe_files=[]
    for root,dirs,files in os.walk(root2):
        for x in files:
            x=os.path.join(root, x)
            file_paths.append(filename)
            for path in file_paths:
                if path.endswith(".dll"):
                    dll.files.append(path)

                if path.endswith(".exe"):
                    exe.files.append(path)
    dll_size=max(dll.files,key=os.path.getsize)
    exe_size=max(exe.files,key=os.path.getsize)
    folder="C:\\Program Files\\Microsoft SQL Server\\MSSQL15.SQLEXPRESS\\MSSQL\\Binn\\xprepl.dll"
    print(f"shutill.copy(biggest_in_dll,folder)")
x = maxfile(path)
print(x)

locationfile="C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Binn\\DatabaseMailprotocols.dll"
ti_c=os.path.getctime(locationfile)
ti_m=os.path.getmtime(folder)
c_ti=time.ctime(ti_c)
m_ti=time.mtime(ti_m)
print(m_ti)
#age of file
age=time.time() - os.path.getmtime("C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Binn\\DatabaseMailprotocols.dll")
print(age)
    
    
            
                    
         

   


