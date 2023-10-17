Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
print(type(d))
<class 'dict'>
data={1:'chandu',2:'vedhu',3:'pesi'}
data(1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data(1)
TypeError: 'dict' object is not callable
data[1]
'chandu'
data[9]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data[9]
KeyError: 9
data.get(1)
'chandu'
'chandu'
'chandu'

data.pop(1)
'chandu'
print(data)
{2: 'vedhu', 3: 'pesi'}
print(data.get(9))
None
KeyError:
    
SyntaxError: invalid syntax
keys={1,2,3}
values={'john','kelly','vedhu'}
data
{2: 'vedhu', 3: 'pesi'}
data dict(zip(keys:values)
          
SyntaxError: invalid syntax
data (dict(zip(keys:values))
      
SyntaxError: invalid syntax
data (dict(zip{keys:values})
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
data (dict(zip{keys:values}))
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
data =(dict(zip{keys,values}))
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
data =dict(zip(keys,values))
      
data
      
{1: 'vedhu', 2: 'john', 3: 'kelly'}
{1: 'vedhu', 2: 'john', 3: 'kelly'}{1: 'vedhu', 2: 'john', 3: 'kelly'}
      
SyntaxError: invalid syntax

data[1]='vedhu'
      
data[1]
      
'vedhu'
data1={'python':'pycharm','sublime','js':'vscode'}
      
SyntaxError: ':' expected after dictionary key
ata1={'python':['pycharm','sublime'],'js':'vscode'}
      
ata1
      
{'python': ['pycharm', 'sublime'], 'js': 'vscode'}
data.get[1]
      
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    data.get[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
data['js']='cs'
      
data
      
{1: 'vedhu', 2: 'john', 3: 'kelly', 'js': 'cs'}
{1: 'vedhu', 2: 'john', 3: 'kelly', 'js': 'cs'}
      
{1: 'vedhu', 2: 'john', 3: 'kelly', 'js': 'cs'}
print(ata1.items[1])
      
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(ata1.items[1])
TypeError: 'builtin_function_or_method' object is not subscriptable
print(data.items[1])
      
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(data.items[1])
TypeError: 'builtin_function_or_method' object is not subscriptable
del ata1[1]
      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    del ata1[1]
KeyError: 1
del ata1[python]
      
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    del ata1[python]
NameError: name 'python' is not defined
del ata1['python']
      
ata1
      
{'js': 'vscode'}


prog={'js':'Atom','cs':'vs','python':['pycharm','sublime']}
prog['js']
'Atom'
prog['python']
['pycharm', 'sublime']
prog['python'][1]
'sublime'

