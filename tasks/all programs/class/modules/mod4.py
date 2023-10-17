x = ['abc.txt',  'mn.txt', '1.py', '2.py', '1.txt', '3.py', 'abc.py.txt']

"""
for f in x:
    if '.py' in f:
        print(f)
"""

# startswith and endswith function

for f in x:
    if f.endswith('.py'):
        print(f)
