#1
def maxVal(a,b):
    if a>b:
        return a
    else:
        return b

print(maxVal(8,2))
print(maxVal(4,5))

#2
def sumVals(x,y,z):
    s=x+y+z
    return s

first=int(input('Enter first value: '))
second=int(input('Enter second value: '))
third=int(input('Enter third value: '))

print('\nSum of entered numbers is:',sumVals(first,second,third))

#3
def isNeg(n):
    if n<0:
        return True
    else:
        return False

n=int(input('Enter the number: '))
if isNeg(n):
    print(n,'is negative number.')
else:
    print(n,'is not negative number.')

#4
def isUpper(ch):
    if ch.isupper():
        return True
    else:
        return False

ch=input('Enter a character: ')
if isUpper(ch):
    print(ch,'is upper case letter.')
else:
    print(ch,'is lower case letter.')

#5
def amtDue(p,q):
    return p*q

price=int(input('Enter the price:'))
quantity=int(input('Enter the quantity:'))
print('\nAmount due:',amtDue(price,quantity))

#6
def lowEquiv(ch):
    return ch.lower()

ch=input('Enter the character: ')
print(lowEquiv(ch))