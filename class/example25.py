# Reading data from the file 
# open --> read  --> close

# To open
"""
To open a file we have function defined i.e open()

The open functuon will  take two params 1. filepath, 2. mode

<fileobjec> open(filepath, mode)

Where the filepath is the loction of the file in your system and its strings

"c:\\abc.txt"
"c:\\desktop\\info.txt"
Where the mode parameter can be eithrt r, w, a

r - reading
w - writing
a - appending

The open() function will retunr the file object
"""
# To read 
"""
To read the data from the file we have function called read()  function

The read function returns data from teh file as a String type
"""
# To close
"""
to close the file we have a function called close()
"""
# open
fobj = open('sample.txt', 'r')
# read
text = fobj.read()
# close
fobj.close()
print(type(text)) # Always check type before you process the data

print("-----------------------------------------")
print(text)








