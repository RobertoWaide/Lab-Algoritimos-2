def apresent(week):
    for i in range(6):
        print(f"\n{list(week.keys())[i]} - Você tem : {list(week.values())[i]}")


def calendar():
    week = {}
    day = ["Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]
    for i in day:
        if i != "Sabado":
            a = input(f"Que aula você tem na {i}-feira: ")
        else:
            a = input(f"Que aula você tem no {i}: ")
        week[i] = a

    return week

def main():
    week = calendar()
    apresent(week)
    

main()
