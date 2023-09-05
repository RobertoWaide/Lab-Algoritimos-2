def verdafake(key):
    verdagreen = input("Procure por sua chave: ").lower()
    if verdagreen in key.keys():
        return True
    else:
        return False


def main():
    key = {
        "faca" : 2 ,
        "panela" : 5 ,
        "espátula" : 2 ,
        "colher" : 3 ,
        "peneira" : 1 ,
        "ralador" : 2}
    print(verdafake(key))
    

main()
