#Create a string made of the middle three charcters

str1:"jhonDipPeta"
#ouptput:Dip

str1="jhonDipPeta"
def get_middle_three_chars(str1):
    print("Original String is",str1)


    mi=int(len(str1)/2)

    #use string slicing to get result charcters
    res=str1[mi-1:mi+2]
    print("middle three chars are:",res)


get_middle_three_chars(str1)
