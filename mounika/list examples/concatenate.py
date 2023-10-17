#Concatenate two lists in following order

#list1=['Hello','take']
#list2=['Dear','sir']

list1=['Hello','take']
list2=['Dear','sir']

result=[x+y for x in list1 for y in list2]
print(result)
