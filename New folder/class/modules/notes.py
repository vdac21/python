Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # math module
>>> # Case1:
>>> 
>>> # SYNATX1:    import <module_name>
>>> 
>>> import math
>>> 
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
>>> # To call a functin inside a module -->  modulename.functionname()
>>> 
>>> # 5! = 5 * 4 * 3 * 2 * 1
>>> 5*4*3*2*1
120
>>> math.factorial(5)
120
>>> math.floor(5.6)
5
>>> 
======================================= RESTART: Shell ======================================
>>> # SYNTAX 2:   from module_name import <function>
>>> from math import factorial
>>> factorial(5)
120
>>> floor(5.6)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    floor(5.6)
NameError: name 'floor' is not defined
>>> 
======================================= RESTART: Shell ======================================
>>> from math import factorial, floor
>>> factorial(5)
120
>>> floor(5.6)
5
>>> 
======================================= RESTART: Shell ======================================
>>> from math import *
>>> factorial(5)
120
>>> floor(5.6)
5
>>> sqrt(4)
2.0
>>> 
======================================= RESTART: Shell ======================================
>>> #  We can alias names to the module or functions inside a module
>>> 
>>> import math as m
>>> 
>>> m.factorial(5)
120
>>> 
======================================= RESTART: Shell ======================================
>>> from math import factorial
>>> 
>>> from math import factorial as f
>>> 
>>> f(5)
120
>>> 