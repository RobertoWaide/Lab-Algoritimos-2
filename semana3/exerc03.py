def cash():
    hund = 0
    fifty = 0
    twelve = 0
    ten = 0
    five = 0
    money = float(input("Insira um valor:"))
    if money % 100 == 0:
        hund = money / 100
    else:
        while money > 100:
            money -= 100
            hund += 1

    if money % 50 == 0:
        fifty = money / 50
    else:
        while money > 50:
            money -= 50
            fifty += 1

    if money % 20 == 0:
        twelve = money / 20
    else:
        while money > 20:
            money -= 20
            twelve += 1

    if money >= 10 :
        money -= 10
        ten += 1

    if money % 5 == 0:
        five += 1

    return hund, fifty, twelve, ten, five


def main():
    hund, fifty, twelve, ten, five = cash()
    if hund > 0:
        print(f"Notas de cem: {hund}")
    if fifty > 0:
        print(f"Notas de cinquenta: {fifty}")
    if twelve > 0:
        print(f"Notas de vinte: {twelve}")
    if ten > 0:
        print(f"Notas de dez: {ten}")
    if five > 0:
        print(f"Notas de cinco: {five}")


main()
