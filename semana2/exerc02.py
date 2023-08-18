def action3(same,list3):
    print(f"Iguais:{same}\nLista:{list3}")

def action2(list1,list2):
    list3 = []

    for i in list1 + list2:
        if i in list3:
            continue
        else:
            list3.append(i)

    return list3

def action1(list1,list2):
    same = []

    for i in list1:
        if i in list2:
            same.append(i)
    
    return same


def main():
    same = action1(list1,list2)
    list3 = action2(list1,list2)
    action3(same,list3)

list1 = [33, 7, 2, 19, 5, 1, 4, 56, 8, 22]
list2 = [5, 1, 8, 34, 5, 17, 6, 12, 9, 23]
main()
