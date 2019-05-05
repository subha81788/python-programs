def getSecondMaximum(ns):
    max1=max2=-10000
    for n in ns:
        if max1 < n and max2 < n:
            max1 = n
        elif max2 < n:
            max2 = n
        print(max1,"\t",max2)
    return max2

numbers = [100,22,-53,9,-7,19,81,95,23,99]
print("Second maximum number is: ", getSecondMaximum(numbers))




