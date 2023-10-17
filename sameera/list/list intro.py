Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
nums=[10,20,30,40]
nums
[10, 20, 30, 40]
[10, 20, 30, 40]
[10, 20, 30, 40]
nums[0]
10
nums[20]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    nums[20]
IndexError: list index out of range
nums[20\]
     
SyntaxError: unexpected character after line continuation character
nums[-2]
     
30
nums[2:]
     
[30, 40]
nums[1:3]
     
[20, 30]
[20, 30]
     
[20, 30]

nums[1:3:2]
     
[20]
[20]
     
[20]
names=["vedhu","lucky","pesi"]
     
names
     
['vedhu', 'lucky', 'pesi']
values=[9.5,'vedhu',6]
     
values
     
[9.5, 'vedhu', 6]
obj=[names,values]
     
obj
     
[['vedhu', 'lucky', 'pesi'], [9.5, 'vedhu', 6]]
nums.append([50])
     
nums
     
[10, 20, 30, 40, [50]]
nums.append(50)
     
nums
     
[10, 20, 30, 40, [50], 50]
[10, 20, 30, 40, [50], 50]
     
[10, 20, 30, 40, [50], 50]
nums.insert[2,45]
     
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    nums.insert[2,45]
TypeError: 'builtin_function_or_method' object is not subscriptable
nums.insert([2,45])
     
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    nums.insert([2,45])
TypeError: insert expected 2 arguments, got 1
nums.insert(9)
     
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    nums.insert(9)
TypeError: insert expected 2 arguments, got 1
nums.insert[2]
     
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    nums.insert[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
nums.insert(1,23)
     
nums
     
[10, 23, 20, 30, 40, [50], 50]
nums.remove(20)
     
nums
     
[10, 23, 30, 40, [50], 50]
nums.pop(2)
     
30
30
     
30
del nums[2:]
     
nums
     
[10, 23]
[10, 23]
     
[10, 23]
nums.extend([25,35,62])
     
nums
     
[10, 23, 25, 35, 62]
[10, 23, 25, 35, 62]
     
[10, 23, 25, 35, 62]
min(nums)
     
10
max(nums)
     
62
sum(nums)
     
155
nums.sort()
     
nums
     
[10, 23, 25, 35, 62]
num=[2,39,7,80]
     
num
     
[2, 39, 7, 80]
num.sort()
     
num
     
[2, 7, 39, 80]
