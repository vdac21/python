import subprocess
 
# traverse the software list
Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
a = str(Data)
# try block
#  arrange the string
try:
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[i])
except IndexError as e:
    print("}")


def filter_services(dict_all_services, service_start_with):
    filtered_dic = {}
    for i in dict_all_services:
        if i[0].startswith(service_start_with):
            fitered_dict [i[0]]=i[1]
    return filtered_dict
a2=input("enter input charcter:")

e2=filter_services(items,a2)
print(e2)










              

