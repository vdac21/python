'''
s={}
print(type(s))
<class 'dict'>
s={1,2,4,5}
print(type(s))
<class 'set'>
s1={1,2,3,5,7,8,0}
s1
{0, 1, 2, 3, 5, 7, 8}

s[2]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
'''

'''
set methods

add()
update()
pop()
remove()
'''
'''
s={1,2,5,8,90,80}
s.add(67)
s.update({90,84,70})
s.pop()
s.remove(90)
print(s)

'''

'''
set operations


union
intersection
subset 
difference

'''

s1={1,2,3,4}
s2={4,5,6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issubset(s2))




