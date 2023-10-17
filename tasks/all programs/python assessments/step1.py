import subprocess
def run_command(cmd):
    try:
        resp=subprocess.check_output(cmd)
        resp=resp.decode('utf-8')
        return resp
    except Exception as e:
        print(f"unable to run the command:(cmd1)")
        print(str(e))

cmd1="tasklist"

output=run_command(cmd1)
print(output)

lines=output.split("\n")[3:]
print(lines)


d={}
x=(lines[0]).split()
#print(x)
p=x[0]+" "+x[1]+" "+x[2]
q=x[3]
d[p]=q
#print(d)

for line in lines[1:]:
    words= line.split()
    #print(words)
    if len(words)>2:
        word=words[0:2]
        #print(word)
        d[word[0]]=word[1]
print(d)
#step2    
items=d.items()
print(items)

def filter_services(dict_all_services, service_start_with):
    filtered_dict = {}
    for i in dict_all_services:
        if i[0].startswith(service_start_with):
            filtered_dict[i[0]]=i[1]
    return filtered_dict

input1=input("enter any string char:")
output2=filter_services(items,input1)
print(output2)



#step3

import os
 
output = os.popen('wmic process get description').read()
 

#print(output)



#step-4
d4={}

#print{d4}

def services_memory(cmd4):
    m4=cmd4.split('\n')[3:]
    for i in m4:
        words4=i.split(" ")
        #print(words)
        if len(words4)>2:
           services=words4[0]
           memory=words4[len(words4)-1]
           d4[services]=memory
    return d4

output4=services_memory(output)
#print(output4)


#step5
def filter_services(service_start_with):
    n=service_start_with("\n")[3: ]
    return n
O5=filter_services(output)
#print(O5)
d5={}
l5=[]
for i in r5[0:len(O5)-1]:
    words5=i.split("  ")
    #print(words5)
    x=words5[len(words5)-1].split()
    #print(x)
    y=[x(0)]
    #print(y)
    z=int(y)//1024
    print(z)

input5=input("enter any service name:")
output5=returns_mb(output)
#print(output5)
    


#step6


def returns_pid(cmd):
    for i in cmd:
        if service_name in i[0]:
            return i[1]

sevice_name=input("enter service name:")

output6=returns_pid(items)
#print(output6)


#step7

def returns_services(cmd):
    for i in cmd:
        if ipd_values in i[1]:
            return i[0]

ipd_values=input("enter ipd value:")

output7=returns_service(items)
#print(output7)


#step8
def get_result(cmd):
    if cmd in char:
       return True
    else:
       return False

input=("enter a char:")
print("true")








