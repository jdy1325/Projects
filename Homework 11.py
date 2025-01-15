#1
def multiply(x, y):
  if y==1:
    return x
  else:
    return x + multiply(x, y-1)

first = 7
second = 4
print(multiply(first,second))


#2
def allSum(numList,start):
  if len(numList) == 0:
      return 0
  elif start >= len(numList):
      return 0
  else:
      return numList[start] + allSum(numList,start + 1)

numbers = [1,3,5,7,9,2,4,6,8]
print(allSum(numbers,0))


#3
def integerSum(value):
    if value == 1:
        return 1

    return value + integerSum(value - 1)

numX = 50
print(integerSum(numX))


#4
def raisePower(value1, value2):
    if value2 == 0:
        return 1
    else:
        return value1*raisePower(value1, value2-1)

numX = int(input("Enter a number: "))
numY = int(input("Enter exponent: "))
print(raisePower(numX, numY))


#5
def ackermann(m, n):
    if m == 0:
        return n + 1

    else:
        if n == 0:
            return ackermann(m - 1, 1)
        else:
            return ackermann(m - 1, ackermann(m, n - 1))

numX = 2
numY = 2
print(ackermann(numX, numY))