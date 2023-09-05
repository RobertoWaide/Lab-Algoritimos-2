def apresent(abc):
    for letter, number in abc.items():
        print(f"{letter}:{number}")

def alphabet():
    abc = {"vogal": 0, "consoante": 0}
    n = input("Digite uma palavra ou frase: ").lower()
    for i in n:
        if i in "aeiou":
            abc["vogal"] += 1
        elif i.isalpha():
            abc["consoante"] += 1
    
    return abc


def main():
    abc = alphabet()
    apresent(abc)

main()
