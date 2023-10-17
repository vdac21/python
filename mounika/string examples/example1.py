#create a string made of the first,middle and last character
#str1=James
#expected output:jms

'''
1.Use string indexing to get the charcter present at the given index
2.use str1[0] to get the first charcter of a string and add it to the result variable.
3.next, get the middle charcters index by diving string length by 2. x= len(str1)/2.Use str1[x] to get  the middle character and add it to the result variable.
4. Use str1[len(str1)-1] to get the last charcter of a string and add the result variable.
5. print result variable to display new string.
'''

str1 = 'james'
#get the  first charcter
res=str1[0]

# get middle index number
mi=int(len(str1)/2)
#get middle charcter and add it to rsult
res=res+str1[mi]
#get last charcter and add
res=res+str1[len(str1)-1]

print("New string:",res)

