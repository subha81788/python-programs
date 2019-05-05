def modify_matrix(mat,r,c):
    row=[0]*r
    col=[0]*c

    for i in range(0,r):
        for j in range(0,c):
            if mat[i][j] == 1:
                row[i] = 1
                col[j] = 1

    for i in range(0,r):
        for j in range(0,c):
            if row[i] == 1 or col[j] == 1:
                mat[i][j] = 1

def print_matrix(mat,r,c):
    for i in range(0,r):
        for j in range(0,c):
            print(mat[i][j], end = " ")
        print()


mat = [ [1, 0, 0, 1], 
        [0, 0, 1, 0], 
        [0, 0, 0, 0] ]  
  
print("Input Matrix") 
print_matrix(mat,3,4) 
  
modify_matrix(mat,3,4) 
  
print("\n\nMatrix after modification") 
print_matrix(mat,3,4)
