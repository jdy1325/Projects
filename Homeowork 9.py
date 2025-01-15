#1
def showMax(a,b,c):
    if (a >= b) and (a >= c):
        print("Alpha is the Largest.")
    elif (b >= a) and (b >= c):
        print("Beta is the largest.")
    else:
        print("Gamma is the largest.")

alpha = int(input("Enter alpha: "))
beta = int(input("Enter beta: "))
gamma = int(input("Enter gamma: "))
showMax(alpha,beta,gamma)


#2
def showVolume(h,r):
    pi = 3.14
    V = pi*(r**2)*h
    print("Volume of cylinder is", V)

radius = float(input("Please enter radius: "))
height = float(input("Please enter height: "))
showVolume(radius, height)


#3
def draw(ch, n):
    print(ch*n)

symbol = input("Please enter the symbol: ")
number = int(input("Please enter the number of occurrences : "))
draw(symbol, number)


#4
def greet():
    print("Hello")
    print("Welcome to my script")
greet()


#5
def showRatio(x, y):
    print("Ratio : ", x/y)

numerator = int(input("Please enter the numerator: "))
denominator = int(input("Please enter the denominator: "))

showRatio(numerator, denominator)