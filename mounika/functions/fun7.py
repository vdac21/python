#lower to upper
'''

def myupper(word):
    word_upper=" "
    for ch in word:
        if ch>='a' and ch<='z':
            ch=chr(ord(ch)-32)
            
        word_upper=word_upper+ch
    return word_upper

s1="vedhu"
s=myupper(s1)
print(s)




r='vedhu'
v=r.upper()
print(v)

'''


s=input("Enter a String:")
result=""
for i in range(0,len(s)):
    ascii_val = ord(s[i])
    if(ascii_val>64 and ascii_val<91):
        result+=chr(ascii_val+32)
    else:
        result+=chr(ascii_val)
s=result
print(s)
