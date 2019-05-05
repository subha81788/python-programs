def squareEvenNums(ns):
    return [n**2 for n in ns if n%2 == 0]

numbers = [24,8,3,17,12,19,25,36,21]
print(squareEvenNums(numbers))
