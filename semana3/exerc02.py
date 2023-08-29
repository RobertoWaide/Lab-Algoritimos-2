
def number(matrix):
    add = 0
    list = []
    for i in range(len(matrix)):
        add += matrix[i][i]
        list.append(matrix[i][i])

    return add, list

def main():
    add,list = number(matrix)
    print(f"{list} \n {add}")


matrix = [
 [ 9, 12,  4,  3,  2,  0, 15,  7],
 [14,  5, 11,  2, 19,  1, 10, 10],
 [ 8, 18,  1, 13,  6, 14, 10, 12],
 [19, 16,  5,  6,  8,  1,  6, 14],
 [ 5,  9, 17, 10, 16,  0,  2, 15],
 [ 2, 17,  7,  7, 11, 13, 19, 18],
 [16, 20,  3,  3,  2,  7, 14,  1],
 [15,  3,  8,  1, 13,  4, 18,  0]]


main()
