def check(list1,list2):
    list3 = [[],[],[]]
    for i in range(3):
        for j in range(3):
            h = list1[i][j] + list2[i][j]
            list3[i].append(h)
    return list3


def main():
    list1 =[[3,9,7],
            [4,1,3],
            [6,7,9]]
    list2 =[[8,4,2],
            [5,1,4],
            [0,3,7]]
    list3 = check(list1,list2)
    print(list3)

main()
