def apresent(list,reverse):
    print(f"{list} \n{reverse}")
    
def invert(list):
    reverse = []

    for i in range(len(list)-1,-1,-1):
        reverse.append(list[i])

    return reverse

def main():
    reverse = invert(list)
    apresent(list, reverse)


list = [15,10,9,4,666,69]
main()
