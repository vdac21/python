#Turn every item of a list into  its square


#numbers=[1,2,3,4,5,6,]
'''
#soultion1:1.Using loop and list method

2.create a empty result list
3.iterate a numbers list using a loop
4.in each iteration, calculate the square of a current number and add it to the result list using the append() method

'''

numbers=[1,2,3,4,5,6,]

result=[]

for i in numbers:
    result.append(i*i)
print(result)

'''
solution2:Use list comprehension
'''

numbers=[1,2,3,4,5,6]
result=[x*x for x in numbers]
print(result)
