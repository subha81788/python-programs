addition = lambda x,y : x + y
subtraction = lambda x,y : x - y
multiplication = lambda x,y : x * y
division = lambda x,y : x / y

while True:
    print("\n\nMENU")
    print("=========================")
    print("1:\tAddition")
    print("2:\tSubtraction")
    print("3:\tMultiplication")
    print("4:\tDivision")
    print("0:\tExit")
    print("=========================")
    ch = int(input("Enter choice: "))
    if ch == 0:
        break
    if ch != 1 and ch != 2 and ch != 3 and ch != 4:
        print("Invalid choice!")
        continue
    a,b,res = 0,0,0.0
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
    if ch == 1:
        res = addition(a,b)
    elif ch == 2:
        res = subtraction(a,b)
    elif ch == 3:
        res = multiplication(a,b)
    else:
        try:
            res = division(a,b)
        except ZeroDivisionError:
            print("Cannot divide by zero")
            continue
    print("Result = ",res)
