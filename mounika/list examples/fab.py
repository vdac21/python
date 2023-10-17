"""
def fab(n):
 if n == 0 :
     
     return 0
 elif n==1:
     return 1
 elif n==2:
     return 1
 else:
     return fab(n-1)+fab(n-2)
 
for i in range(5):
 print(fab(i), end = ', ')





 the sequence of numbers in which each number in the sequence is equal to the sum of two numbers before it. 








0
0+1=1
1+1=2
1+2=3
3+2=5
5+3=8
"""
def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a+b
  return a

# Generate the first ten numbers in the Fibonacci series
for i in range(20):
  print(fibonacci(i))
