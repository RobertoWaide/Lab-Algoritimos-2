def main():
    names = {
        "Arthur" : "Preta",
        "Ana" : "Amarela",
        "Sofia" : "Azul",
        "Miguel" : "Verde",
        "Luiz Yan" : "Vermelha"
    }
    for i in range(len(names)):
        print(f"{list(names.keys())[i]} está de camiseta {list(names.values())[i]}\n")



main()
