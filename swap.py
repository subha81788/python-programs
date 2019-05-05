x,y = [int(a) for a in input("Enter two integers:").split(" ")]

print("You entered:",x,y)

x,y = y,x
print("After swap:",x,y)
