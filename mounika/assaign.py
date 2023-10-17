#1.Wap print all duplicate elements from the given list
   #x=[10,25,28,10,78,26,25,35,28]
  #output=[10,25,28] 
 
x=[10,25,28,10,78,26,25,35,28]
original=[]
duplicate=[]
for i in x:
    if i not in original:
        original.append(i)
    else:
        duplicate.append(i)
print(original)
print(duplicate)

#2.Concatenate two lists index-wise
 # list1=["M","Na","i","Ke"]
  #list2=["y","me","s","lly"]

  #Note:Use the Zip() function. This function takes two or more iterables(like      list,dict,string),aggregates them in a tuple ,and returns it.


list1=["M","Na","i","Ke"]
list2=["y","me","s","lly"]
#print(list(zip(list1,list2)))
list3=[i+j for i,j in zip(list1,list2)]
print(list3)

#5.Concatenate two lists in following order
#list1=['Hello','take']
#list2=['Dear','sir']

list1=['Hello','take']
list2=['Dear','sir']
list3=list1+list2
print(list3)

#4.Turn every item of a list into  its square
# numbers=[1,2,3,4,5,6,]

numbers=[1,2,3,4,5,6]
n2=[i*i for i in numbers]
print(n2)

#3.Reverse a list in python
  #list1 =[100,200,300,400,500]

list1 =[100,200,300,400,500]
print(list1[::-1])
