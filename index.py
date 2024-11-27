# Importando biblioteca para comandos do sistema operacional
import sys

# Definindo a lista de produtos
estoque = []

# Função para adicionar produto ao estoque
def adicionarProdutos(nome, quantidade, preco):
    produto = {"nome": nome, "quantidade": quantidade, "preço": preco*quantidade}
    estoque.append(produto)  # Aqui está um erro proposital, deveria ser append
    print(f"Produto {nome} adicionado ao estoque!")

# Função para listar todos os produtos no estoque
def listarProdutos():
    if not estoque:  # Condição errada; deveria verificar se a lista está vazia com "if not estoque"
        print("Estoque vazio.")
    else:
        print("Produtos em estoque:")
        for i, produto in enumerate(estoque):
            print(f"{i + 1}. Nome: {produto['nome']}, Quantidade: {produto['quantidade']}")

# Função para atualizar a quantidade de um produto
def atualizar_quantidade(produto, quantidade ):
    if indice < len(estoque) and indice > 0:  # Condição está invertida; deveria ser "indice >= 0"
        estoque[indice]["quantidade"] == nova_quantidade  # Uso de "==" em vez de "="
        print("Quantidade atualizada com sucesso!")
    else:
        print("Produto não encontrado.")

# Função para excluir um produto do estoque
def excluir_produto(indice):
    if indice > 0 or indice < len():  # Condição lógica errada; deveria ser "indice >= 0 and indice < len(estoque)"
        produto_excluido = estoque.remove(indice)  # Erro: deveria usar pop(indice)
        print(f"Produto {produto_excluido['nome']} removido do estoque.")
    else:
        print("Índice inválido.")

# Loop principal
while True:  # Erro: duplicação de "while"
    print("\nMenu de Controle de Estoque:")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Atualizar quantidade de produto")
    print("4. Remover produto")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade inicial: "))
        preco = float(input("Digite o preço do produto: "))
        adicionarProdutos(nome, quantidade, preco)
    elif opcao == "2":
        print(estoque)
    elif opcao == "3":  # Menu sem opção de listar produtos (erro de menu)
        listarProdutos()
        indice = int(input("Digite o índice do produto que deseja atualizar: ")) - 1
        nova_quantidade = int(input("Digite a nova quantidade: "))
        atualizar_quantidade(indice, nova_quantidade)
    elif opcao == "4":
        indice = int(input("Digite o índice do produto que deseja excluir: "))
        excluir_produto(indice)
    elif opcao == "5":
        print("Encerrando o programa. Até logo!")
        print("3x1 pro Racing")
        break
    else:
        print("Opção inválida, tente novamente.")