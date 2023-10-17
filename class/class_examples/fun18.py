#WAF to reverse a list
"""
def myreverse(x_list):
    y=[]
    for i in range(len(x_list)-1,-1,-1):
        y.append(x_list[i])
    return y

x=[1,2,3,4,5,5]
print(f"input list:{x}")
s=myreverse(x)
print(f"Reversed list: {s}")



mylist=[1,2]
reverse(mylist)
print(reverse)
"""

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
 
 
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
