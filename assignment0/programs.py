#1)WAP to accept two integers and weather they are equal or not.
x = 90
y = 80
if (x == y):
    print('equal')
else:
    print('not equal')
#2)WAP to check weather a given number is even or odd.
a = 7
if (a % 2)== 0:
    print('even number')
else:
    print('odd number')
#3)WAP to check weather a given number is positive or negative.
x = 110
if x > 0:
    print('positive number')
elif x==0:
    print('zero')
else:
    print('negative number')
#4)WAP to find weather a given year is leap year or not.
year=2016
if (year%2==0 and year%100!=0 or year%200==0):
     print('leap year')
else:
    print('not leap year')
#5)WAP to find largest two numbers.
a = 70
b = 90
if a > b:
    print('largest number')
else:
    print('smallest number')
#6)WAP to find largest three numbers.

num1 = 18
num2 = 14
num3 = 16
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
#7)WAP to read the age of a candidate and determine whether it is eligible for casting his\her own vote.
age = int(input("Enter Age : "))

# condition to check voting eligibility
if age>=18:
    status="Eligible"
else:
    status="Not Eligible"

print("You are ",status," for Vote.")
#8)WAP to check whether a character is an alphabet,digit or special character.
ch = input("Please Enter Your Own Character : ")

if(ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")
elif(ch.isalpha()):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is a Special Character")
#9)WAP to check whether an alphabet is a vowel or consonant.
x = input("Enter an alphabet : ")
if x in ('a', 'e', 'i', 'o', 'u'):
    print('vowel')    
else:
    print('Consonant')
#10)WAP to calculate profit and loss on a transaction from the given cost price and selling price
sp,cp = 2000, 2000
if sp>cp:
    #Profit = (sp - cp)
    print('profit')
elif sp==cp:
    print('equal')
else:
    #Loss = (cp - sp)
    print('loss')
#11)WAP to read the value of an integer m and display the value of n is 1 where m is larger than 0, 0 when m is 0 and -1 when m is less than 0.
m = -20
if m>0:
    print('n is 1')
elif m<0:
    print('-1')
elif m==0:
    print('0')
else:
    print('n is not 1')

#12)
x =140
if x<150:
    print("DWARF")
elif x>=150<165:
    print("AVERAGE HEIGHT")
elif x>165:
    print("TALL")
else:
    print("program over")


#13)
x = -2
if x<0:
    print('freezing weather')
elif 0-10:
    print('very cold weather')
elif 10-20:
    print('cold weather')
elif 20-30:
    print('normal temp')
elif 30-40:
    print('its hot')
elif x>=40:
    print('its very hot')
else:
    print('program over')


#14)
x = 30
if x>=60:
    print('first class')
elif x<60>=48:
    print('second class')
elif x<48>=36:
    print('pass')
elif x<36:
    print('fail')


#15)
m = 65
p = 55
c = 55
if m>=65:
    print('maths pass')
elif p>=55:
    print('physics pass')
elif c>=50:
    print('chemistry pass')
elif m+p+c>=180 or m+p>=140:
    print('eligible for admmission')
else:
    print('not eligible')












