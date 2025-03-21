from rich.console import Console
console = Console()
estoque = [
    [10,12,15],
    [22,24,16], 
    [15,6,35] 
]

produtos = ["Tesoura" , "Machado" , "Caderno"] 
armazens_estoque = ['Pau dos Ferros', 'Doutor Severiano', 'São Francico do Oeste']

def exibir_estoque(estoque,produtos):
    print()
    console.print("[bold cyan]Estoque Atual:[/bold cyan]")
    for l in range(len(estoque)):
        print(f"{produtos[l]}: {estoque[l]}")     

def adicionar_produto(estoque,produtos):
    print()
    linha_nova = []     
    print('Adicone o novo produto!')
    produtos.insert(0,input("Qual será o produto adicionado? "))
    for armazens in range(len(estoque[0])):
        linha_nova.append (int(input(f"Quantos produtos possui no armazém de {armazens_estoque[armazens]}: ")))
    estoque.insert(0,linha_nova)
    print('Produto adicionado!')
    return estoque

def editar_quantidade():
    print()
    print('Produtos do estoque:')
    for products in range(len(produtos)):
        print(f"{products + 1}. {produtos[products]}")
    editar = int(input('Escolha o produto que deseja editar: '))
    print()
    print('Armazens do estoque: ')
    for armazens in range(len(armazens_estoque)):
        print(f"{armazens + 1}. {armazens_estoque[armazens]}")
    editar2 = int(input('Escolha o armazém: '))
    quantidade_nova = int(input('Qual será a quantidade atual do produto?: '))
    estoque[editar - 1][editar2 - 1] = quantidade_nova
    print('Quantidade atualizada!')
    return estoque

def remover_produto(estoque,produto):
    print()
    print("Produtos disponiveis:")
    for i in range(len(produtos)):
        print(f"{i+1}. {produto[i]}")
    k = int(input(" Qual produto deseja retirar? "))
    estoque.pop(k-1)
    produtos.pop(k-1)

def pesquisar_produto_por_armazem():
    print()
    for products in range(len(produtos)):
        print(f"{products + 1}. {produtos[products]}")
    ex_produto = int(input('Escolha o produto para exibir sua quantidade: '))
    for armazens in range(len(armazens_estoque)):
        print(f"{armazens + 1}. {armazens_estoque[armazens]}")
    ex_armazem = int(input('Escolha o armazém: '))
    print(f'A quantidade de {produtos[ex_produto - 1]} no armazém {armazens_estoque[ex_armazem - 1]} é: {estoque[ex_produto -1 ][ex_armazem -1 ]}')

def menu():
    print()
    print("-------------------------------")
    print("Sistema de Controle de Estoque:")
    print("-------------------------------")
    print()
    print("1. Exibir Estoque")
    print("2. Cadastrar Produto")
    print("3. Editar Quantidade")
    print("4. Remover Produto")
    print("5. Pesquisar Produto por Armazém")
    print("6. Sair")
    print()
    return input("Escolha uma opção: ")

while True:
    opcao = menu()
    if not opcao.isdigit():
        console.print('[bold red]Entrada inválida! Por favor digite apenas números.[/bold red]')
        continue
    opcao = int(opcao)
    
    if opcao == 1:
        exibir_estoque(estoque, produtos)
    elif opcao == 2:
        adicionar_produto(estoque, produtos)
    elif opcao == 3:
        editar_quantidade()
    elif opcao == 4:
        remover_produto(estoque, produtos)
    elif opcao == 5:
        pesquisar_produto_por_armazem()
    elif opcao == 6:
        print()
        console.print("[bold yellow]Saindo do sistema...[/bold yellow]")
        break
    else:
        console.print("[bold red]Opção inválida, Digite um número válido![/bold red]")  