import subprocess
def run_command(cmd):
    try:
        resp=subprocess.check_output(cmd)
        resp=resp.decode('utf-8')
        return resp
    except Exception as e:
        print(f"unable to run the command:(cmd1)")
        #print(str(e)):

cmd1="tasklist"

output=run_command(cmd1)
#print(output)

lines=output.split("\n")[3:]
#print(lines)


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
 
output3 = os.popen('wmic process get description').read()
 

print(output3)

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
print(output4)

#step5

def return_mb(cmd5):
    m5=cmd5.split("\n")[3:]
    for x in m5[0:len(m5)-1]:
        words=x.split(" ")
        services5=words[0]
        memory5=words[len(words)-1]
        a=memory5.split()
        b=a[0].split(",")
        c=int("".join(b))
        d=c//1024
        d5[services5]=d
        dict_items=d5.items()
        for i in dict_items:
            if input5 in i[0]:
                return i[1]

input5=input("enter service name:")
output5=return_mb(output)
print(output5)



#step6
def get_pid(cmd):
    for i in cmd:
        if service_name in i[0]:
            return i[1]

sevice_name=input("enter service name:")

output6=get_pid(items)
print(output6)




#step7

def get_services(cmd):
    for i in cmd:
        if ipd_values in i[1]:
            return i[0]

ipd_values=input("enter ipd value:")

output7=get_services(items)
print(output7)


#step8

def boolean_condition(cmd):
    for i in cmd:
        if i[0].startswith (input_character):
            return true

input_character=input("enter any string:")
output8=boolean_condition(items)

print(output8)
