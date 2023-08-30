def robb(matrix):
    bigger = 0
    for line in range(len(matrix)):
        side = 1
        horiz = 1
        for colune in range(len(matrix)):
            side *= matrix[line][colune]
            horiz *= matrix[colune][line]
        if side > bigger:
            bigger = side
            
        if horiz > bigger:
            bigger = horiz
    diag = 1
    rev_diag = 1
    for i in range(len(matrix)):
        diag *= matrix[i][i]
    for i in range(len(matrix)-1,-1,-1):
        rev_diag *= matrix[i][i]
    if rev_diag > diag:
        diag = rev_diag
    if diag > bigger:
        bigger = diag

    return bigger


def main():
    bigger = robb(matrix)
    print(bigger)


matrix = [[27, 12,  3, 38, 20],
          [41, 14, 31,  7,  5],
          [18, 29,  8, 43, 16],
          [25, 34, 40,  2, 22],
          [ 9, 35, 23, 42, 11]]

main()
