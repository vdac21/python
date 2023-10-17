#

def myupper(word):
    word_upper = ""
    for ch in word:
        if ch >= 'a' and ch <= 'z':
            ch = chr(ord(ch)-32)
            word_upper = word_upper


        return word_upper


s1 = "hyderabad"


#r = s1.upper()    

myupper(hyderabad)
