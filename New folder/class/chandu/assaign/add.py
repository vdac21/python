list1=[10,3,44,55,67]
list2=[20,45,56,23,12]
l1=len(list1)
l2=len(list2)
if(l1==l2):
     for x in range(0,l1):
          list1[x]+=list2[x]
     print(list1)     
