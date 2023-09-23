import datetime

def cutter(storage,produc,archived):
    historic = []
    if storage[produc]["historic"] != []:
        historic = storage[produc]["historic"]
    historic.append(storage[produc]["price"])
    archived[produc] = historic
    storage.pop(produc)
    return storage,archived

def delete_item(storage,archived):
    if storage == {}: ##Impede a função se o estoque esta vazio e avisa o usuario
        print("\nNão há nenhum item no estoque para deletar")
    else:
        produc = input("\nDigite o produto à remover:\n").upper()
        if produc not in storage:
            print(f"\nO produto {produc} não há em estoque")
        else:
            cutter(storage,produc,archived)
            print("\nRemoção bem sucedida!")
            
    return storage,archived

def filter_sell(name, statement):
    name_upper = name.upper()
    return any(name_upper in line.upper() for line in statement)

def search_category(storage):
    if storage == {}:
        print("\nNão há produtos no seu estoque")
    else:
        category = input("\nDigite a categoria que busca:\n").upper()
        print(f"\nProdutos da categoria {category} encontrados:")
        for item, info in storage.items():
            if info["category"] == category:
                print(f"\nNome do produto: {item} \nQuantidade: {info['quantity']} \nPreço: {info['price']:.2f} \nCategoria: {info['category']}")
                if info["historic"] != []:
                    print(f"Historico de preço: {info['historic']}")
                        
def change_price(storage):
    if storage == {}:
        print("\nSeu estoque não há produtos")
    else:
        historic = []
        produc = input("\nQual produto deseja mudar o preço:\n").upper()
        if produc not in storage:
            print(f"\nO produto {produc} não está no estoque")
        else:
            if storage[produc]["historic"] == []:
                historic.append(storage[produc]["price"])
            else:
                historic = storage[produc]["historic"]
            while True:
                price_str = input("\nDefina o novo preço do produto:\n").replace(",", ".") ## Permite numeros com virgula
                if price_str.replace(".","",1).isdigit(): ## Aprova apenas digitos
                    break
                else:
                    print("\nPreço inválido. Digite um número válido.")
            price = float(price_str) ## Converte para float
            historic.append(price)
            storage[produc]["price"] = price
            storage[produc]["historic"] = historic
            print("\nProduto modificado com sucesso!")

        return storage

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

def register(produc,quantity,storage,statement,cut,archived):
    price = storage[produc]["price"]
    price *= quantity ## Calculo do valor da venda
    current_datetime = datetime.datetime.now() 
    formatted_datetime = current_datetime.strftime("%d/%m/%y - %H:%M:%S") # Formatar a data e hora como uma string
    statement.append(f"Produto: {produc} \nQuantidade vendida: {quantity}\nTotal da Venda: {price:.2f}\nData e hora:\n{formatted_datetime}")
    if cut == True: ## Verificador se é para cortar do estoque
        cutter(storage,produc,archived)

    return storage, statement, archived

def sell(storage,statement,archived):
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

    return storage,statement,archived

def list_all(storage,statement):
    if storage != {}: ##Impede a função se o estoque esta vazio e avisa o usuario
        line = 0 ## Ajuda a configurar o layot do print da linha 61
        print("")
        for item, info in storage.items(): ## Faz a listagem dos itens um a um
            print(f"Nome do produto: {item} \nQuantidade: {info['quantity']} \nPreço: {info['price']:.2f} \nCategoria: {info['category']}")
            if info["historic"] != []:
                print(f"\nHistorico de preço: \n{info['historic']}")

            if any(item in lines.upper() for lines in statement):
                    print(f"\nVendas anteriores:")
                    for lines in statement:
                        if item in lines.upper():
                            print(f"{lines}\n")
            line += 1
            if line < len(storage): ## Ele não apresenta o print na ultima linha]
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

def add(storage,archived):
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

        category = input("\nDigite a categoria do produto\n").upper()

        if produc in archived:
            historic = archived[produc]
        else:
            historic = []
        storage[produc] = {"quantity": quantity , "price":price , "category": category , "historic" : historic}
    else:
        print(f"\nO produto {produc} já havia registro no estoque")
        storage[produc]["quantity"] += quantity ## Se ja existe, só adiciona

    print("\nAdição concluida! :D ")
    return storage

def main():
    storage = {} ## Dicionario // estoque
    statement = [] ## Extrato
    archived = {}
    while True:   ##Sistema basico de menu usando while
        print("\n|1 - Adicionar um produto.     |\n|2 - Buscar por produto.       |\n|3 - Buscar por categoria.     |\n|4 - Visualizar estoque.       |\n|5 - Vender um produto.        |\n|6 - Alterar valor do produto. |\n|7 - Relatório de Vendas.      |\n|8 - Excluir produto.          |\n|9 - Sair.                     |")
        option = input("\nDigite uma opção: ")

        if option == "1":
            add(storage,archived) ##Adiciona
        elif option == "2":
            search(storage) ##Busca
        elif option == "3":
            search_category(storage)
        elif option == "4": 
            list_all(storage,statement) ##Lista estoque 
        elif option == "5": 
            sell(storage,statement,archived) ##Vende
        elif option == "6":
            change_price(storage)
        elif option == "7":
            list_statement(statement) ##Lista Vendas
        elif option == "8":
            delete_item(storage,archived)
        elif option == "9":
            print("\nBye Byeeee~ XOXO S2\n") ##Sai
            break
        else:
            print("\nOpção invalida") ##Invalido

main()
