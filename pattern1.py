def drawPattern(n):
    for i in range(1,n+1):
        for j in range(n-i+1,0,-1):
            print(j,end=" ")
        print()

if __name__ == "__main__":
    r = int(input("Enter the number of rows:"))
    drawPattern(r)
