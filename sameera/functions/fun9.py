def myupper(word):
    word_upper=" "
    for ch in word:
        if ch>='a' and ch<='z':
            ch=chr(ord(ch)-32)
        word_upper=word_upper+ch
    return word_upper
s1="ongole"
s=myupper(s1)
print(s)
        
