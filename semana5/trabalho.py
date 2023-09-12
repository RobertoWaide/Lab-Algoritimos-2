def list_statement(statement):
    if statement == []: ##Impede a função se o extrato estiver vazio e avisa o usuario
        print("\nNãp foi realizado nenhuma compra até este momento.")
    else:
        line = 0 ## Ajuda a configurar o layot do print da linha 12 
        print("")
        for item in statement:
            print(item)
            line += 1
            if line < len(statement): ##Ele não apresenta o print na ultima linha
                print("--------------")

def register(produc,quantity,storage,statement,cut):
    price = storage[produc]["price"]
    price *= quantity ## Calculo do valor da venda
    statement.append(f"Produto: {produc} \nQuantidade vendida: {quantity}\nTotal da Venda: {price:.2f}")
    if cut == True: ## Verificador se é para cortar do estoque
        storage.pop(produc)

    return storage, statement


def sell(storage,statement):
    if storage == {}: ##Impede a função se o estoque esta vazio e avisa o usuario
        print("\nNão é possivel realizar uma venda devido ao estoque estar vazio.")
    else:
        produc = input(f"\nQual produto você deseja vender do estoque:\n").upper()

        if produc in storage: ## Verifica se o produto está disponivel no estoque
            stock  = storage[produc]["quantity"] ## Faz um estoque recente do produto expecifico
            while True: ## Permite apenas valores validos
                try:
                    quantity = int(input(f"\nQuantos {produc} deseja vender? ")) ## Quantidade de compra
                    if quantity < stock: ## Aprova se a compra for menor que o estoque
                        cut = False
                        storage[produc]["quantity"] -= quantity ## Diminui do estoque
                        break
                    elif quantity == stock: ## Corta o item do estoque
                        cut = True
                        break
                    else:
                        print("\nValor pedido acima do estoque")
                except ValueError:
                    print("\nQuantidade inválida. Digite um número inteiro.")
            register(produc,quantity,storage,statement,cut) ## Registra em uma lista
            print("\nVenda realizada!")
        else:
            print(f"\nO produto {produc} não esta disponivel no estoque.")

    return storage,statement


def list_all(storage):
    if storage != {}: ##Impede a função se o estoque esta vazio e avisa o usuario
        line = 0 ## Ajuda a configurar o layot do print da linha 61
        print("")
        for item, info in storage.items(): ## Faz a listagem dos itens um a um
            print(f"Nome do produto: {item} \nQuantidade: {info['quantity']} \nPreço: {info['price']:.2f}")
            line += 1
            if line < len(storage): ## Ele não apresenta o print na ultima linha
                print("-------------------------")
    else:
        print("\nEi negão, tu não tem porra nenhuma aqui seu bosta.")

def search(storage):
    if storage == {}: ##Impede a função se o estoque esta vazio e avisa o usuario
        print("\nO estoque está atualmente vazio.")
    else:    
        produc = input("\nDigite o produto que deseja procurar no estoque:\n").upper()

        if produc in storage: ## Verifica se há o item
            quantity = storage[produc]["quantity"] ## Puxa os dados especificos do item
            price = storage[produc]["price"]     ## V
            print(f"\nO produto {produc} se encontra no estoque com {quantity} unidades, com cada unidade custando R${price:.2f}.")
        else:
            print(f"\nO produto {produc} não se encontra disponível.")


def add(storage):
    produc = input("\nDigite um produto que voçe deseja adicionar ao seu estoque: \n").upper() #upper para facilitar a busca pelo item
    while True: ## while para passar apenas valor int
        try:
            quantity = int(input("\nDigite quanto de quantidade você deseja adicionar ao seu estoque: \n"))
            break
        except ValueError: ## Reinicia caso valor seja invalido
            print("\nQuantidade inválida. Digite um número inteiro válido.")

    if produc not in storage:
        while True:
            price_str = input("\nDefina um preço ao seu produto adicionado:\n").replace(",", ".") ## Permite numeros com virgula
            if price_str.replace(".","",1).isdigit(): ## Aprova apenas digitos
                break
            else:
                print("\nPreço inválido. Digite um número válido.")
        price = float(price_str) ## Converte para float
        storage[produc] = {"quantity": quantity , "price":price}
    else:
        print(f"\nO produto {produc} já havia registro no estoque")
        storage[produc]["quantity"] += quantity ## Se ja existe, só adiciona

    print("\nAdição concluida! :D ")
    return storage


def main():
    storage = {} ## Dicionario // estoque
    statement = [] ## Extrato
    while True:   ##Sistema basico de menu usando while
        print("\n|1 - Adicionar um produto. |\n|2 - Buscar por produto.   |\n|3 - Visualizar estoque.   |\n|4 - Vender um produto.    |\n|5 - Relatório de Vendas.  |\n|6 - Sair.                 |")
        option = input("\nDigite uma opção: ")

        if option == "1":
            add(storage) ##Adiciona
        elif option == "2":
            search(storage) ##Busca
        elif option == "3": 
            list_all(storage) ##Lista estoque 
        elif option == "4": 
            sell(storage,statement) ##Vende
        elif option == "5":
            list_statement(statement) ##Lista Vendas
        elif option == "6":
            print("\nBye Byeeee~ XOXO S2\n") ##Sai
            break
        else:
            print("\nOpção invalida") ##Invalido

main()
