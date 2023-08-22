def im_gonna_go_crazy(group):
    groups = []
    for i in group:
        groups.append(str(i))
    for i in range(len(groups)):
        groups[i] = groups[i].replace(", ", "-")
    #print(groups)
    for i in groups:
        print(i,end=",")

def check(list):
    group = []
    j = []
    for i in list:
        if i-1 not in list or i+1 not in list:
            j.append(i)
            if i+1 not in list:
                group.append(j)
                j = []
                
    #print(group)
    return group


def main():
    list = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]
    group = check(list)
    im_gonna_go_crazy(group)


main()
