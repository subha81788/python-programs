def drawStars(n):
    k = 2*n - 2

    for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ") 
        for j in range(0, i+1): 
            print("* ", end="") 
        print() 
        k = k - 2
  
if __name__ == "__main__":
    drawStars(5)
