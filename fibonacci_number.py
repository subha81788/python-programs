import math

def isPerfectSqaure(x):
    i = int(math.sqrt(x))
    return i*i == x

def isFibonacciNumber(x):
    return isPerfectSqaure(5*x*x + 4) or isPerfectSqaure(5*x*x - 4)


n = int(input("Enter a number: "))
if(isFibonacciNumber(n) == True):
    print(n, "is a fibonacci number")
else:
    print(n, "is not a fibonacci number")
