x=['abc.txt','mn.txt','1.py','2.py','1.txt','3.py','abc.py.txt']

"""
for f in x:
  if '.py' in f:
  print(f)
"""

#starts with and endswith function

for f in x:
    if f.endswith('.txt'):
        print(f)
