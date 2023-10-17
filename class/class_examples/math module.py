Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#math module
#Case1

#SYNTAX1: import <module_name>

import math
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
#to call a function inside module-->modulename.functionname()

#5!=5*4*3*2*1
5*4*3*2*1
120
math.factorial(5)
120
math.floor(5.6)
5


#SYNTAX2: from module_name import <function>
#SYNTAX2: from module_name import <function>

from math import factorial
factorial(5)
120
floor(5.6)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    floor(5.6)
NameError: name 'floor' is not defined. Did you mean: 'float'?


factorial(5)
120
floor(5.6)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    floor(5.6)
NameError: name 'floor' is not defined. Did you mean: 'float'?
import math from *
SyntaxError: invalid syntax
from math import *
factorial(5)
120
floor(5.6)
5
sqrt(2)
1.4142135623730951
sqrt(4)
2.0


#We can alias names to the module or functions inside a module

import math as m
m.factorial(5)
120


from math import factorial

from math import factorial as f
f(5)
120
f(6)
720
