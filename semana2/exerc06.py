def question_block(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return False
        
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def main():
    print(symmetric,question_block(symmetric))
    print(not_symmetric,question_block(not_symmetric))


symmetric = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]]

not_symmetric = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

main()
