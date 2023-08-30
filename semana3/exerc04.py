def robb(matrix):
    n = len(matrix)
    bigger = 0
    
    for line in range(n):
        side = 1
        horiz = 1
        for colune in range(n):
            side *= matrix[line][colune]
            horiz *= matrix[colune][line]
        
        if side > bigger:
            bigger = side   
        if horiz > bigger:
            bigger = horiz
    

    diag = 1
    rev_diag = 1
    
    for i in range(n):
        diag *= matrix[i][i]
        rev_diag *= matrix[i][n - i - 1]    
    if rev_diag > diag:
        diag = rev_diag    
    if diag > bigger:
        bigger = diag


    return bigger



def main():
    matrix = [[27, 12,  3, 38, 20],
              [41, 14, 31,  7,  5],
              [18, 29,  8, 43, 16],
              [25, 34, 40,  2, 22],
              [ 9, 35, 23, 42, 11]]
              
    bigger = robb(matrix)
    print(bigger)

main()
