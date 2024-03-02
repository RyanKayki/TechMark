import os

#Criação de dicionário com a lista de participantes
cod_produto = []
nome = []
preco_un = []
quantidade = []
estoque = []

# FUNÇÕES
def produto_cadastrado(nome_produto):
    for produto in estoque:
        if produto['nome'] == nome_produto:
            return True
    return False

# OPÇÃO 1 - Cadastrar novo produto
def cadastrar():
    nome_produto = input("Informe o nome do novo produto: ")
    if not produto_cadastrado(nome_produto):
        quantidade = int(input("Informe a quantidade inicial: "))
        preco_un = float(input("Informe o preço unitário: "))
        produto = {'nome': nome_produto, 'quantidade': quantidade, 'preco_un': preco_un}
        estoque.append(produto)
        print(f"Produto {nome_produto} cadastrado no estoque.")
    else:
        print(f"Produto {nome_produto} já cadastrado.")

# OPÇÃO 2 - Adicionar produto ao estoque
def adicionar():
    nome_produto = input("Informe o nome do produto a ser adicionado: ")
    if produto_cadastrado(nome_produto):
        quantidade = int(input("Informe a quantidade a ser adicionada: "))
        for produto in estoque:
            if produto['nome'] == nome_produto:
                produto['quantidade'] += quantidade
                produto['preco_un'] == preco_un
                print(f"Produto {nome_produto} adicionado ao estoque.")
                break
    else:
        print(f"Produto {nome_produto} não cadastrado. Cadastre o produto antes de adicionar.")

#OPÇÃO 3 - Consultar quantidade
def consultar():
    try:
        cod_produto = int(input("Informe o código do produto: "))
        produto = estoque[cod_produto]
        print(f"Quantidade disponível de {produto['nome']}: {produto['quantidade']}")
    except IndexError:
        print("Código de produto inválido.")
    except ValueError:
        print("Código de produto deve ser um número.")

#OPÇÃO 4 - Saída de produto(VENDA)
def saida():
    try:
        cod_produto = int(input("Informe o código do produto: "))
        quantidade_vendida = int(input("Informe a quantidade vendida: "))
        produto = estoque[cod_produto]
        if produto['quantidade'] >= quantidade_vendida:
            produto['quantidade'] -= quantidade_vendida
            print(f"{quantidade_vendida} unidades de {produto['nome']} vendidas.")
        else:
            print("Quantidade insuficiente em estoque.")
    except IndexError:
        print("Código de produto inválido.")
    except ValueError:
        print("Código de produto ou quantidade vendida inválidos.")

#OPÇÃO 5 - Gerar lista
def listar():
    print("Produtos disponíveis no estoque:")
    for i, produto in enumerate(estoque):
        print(f"{i} - {produto['nome']}, Quantidade: {produto['quantidade']}, Preço Unitário: {produto['preco_un']}")

#MENU PRINCIPAL
while True:
    os.system('cls')
    print("*** LOJAS TECHMARK - GESTÃO DE ESTOQUE ****")
    print("MENU")
    print("Código [1] - Cadastrar novo produto")
    print("Código [2] - Adicionar produto ao estoque")
    print("Código [3] - Consultar quantidade")
    print("Código [4] - Saída de produto (VENDA)")
    print("Código [5] - Gerar lista do estoque")
    print("Código [6] - Sair do sistema")

    #Validação do MENU
    try:
        op_menu = int(input("Informe o código da opção desejado: "))
        op_menu = int(op_menu)
        if op_menu == 1:
            cadastrar()
        elif op_menu == 2:
            adicionar()
        elif op_menu == 3:
            consultar()
        elif op_menu == 4:
            saida()
        elif op_menu == 5:
            listar()           
        elif op_menu == 6:
            print("Saindo do sitema....")
            break
        else:
            print("Código inválido!")
    except:
        print("Valor inválido!")  
        
    os.system('pause')