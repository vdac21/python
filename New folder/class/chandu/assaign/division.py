2.divison to the list



numbers=input("enter the number list").split(',')
num_list=list(numbers)
print(num_list)
num_list2=[]
def divisible(num_list):
    for num in num_list:
        if(int(num) % 3==0 and int(num) % 2!=0):
            num_list2.append(num)
    return(num_list2)

divisible(num_list)
print(num_list2)
