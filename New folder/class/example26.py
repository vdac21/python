
fobj = open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt", 'r')
text = fobj.read()
fobj.close()


# Writing data inside a file
# open

f = open("C:\\Users\\BHGYALAKSHMI\\OneDrive\\Desktop\\vedhu.txt", 'w')

# write
f.write("Hello")

# close
f.close()
