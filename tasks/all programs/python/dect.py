Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ist = { "ra": "rathamma", "ba": "bhagi"}

ist
{'ra': 'rathamma', 'ba': 'bhagi'}
ist["ga"]=["gopi"]
ist(ga)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    ist(ga)
NameError: name 'ga' is not defined
ist
{'ra': 'rathamma', 'ba': 'bhagi', 'ga': ['gopi']}
ist(ra)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ist(ra)
NameError: name 'ra' is not defined
ist[ga]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ist[ga]
NameError: name 'ga' is not defined
ist["ga"]
['gopi']
ist["ve"]=["vedanth"]
ist
{'ra': 'rathamma', 'ba': 'bhagi', 'ga': ['gopi'], 've': ['vedanth']}
ist["su"]=["susmitha,dummy"]
ist
{'ra': 'rathamma', 'ba': 'bhagi', 'ga': ['gopi'], 've': ['vedanth'], 'su': ['susmitha,dummy']}
