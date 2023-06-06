# Função menu para identificação do usuário
def menu():
    n = 0
    print('\n--- Menu ---\n')
    print('Bem Vindo ao Cadastro do EcoByte!! \n Escolha uma opção: \n 1 - Sou Agricultor \n 2 - Represento a Secretaria da Educação \n')
    resposta = int(input('\n Digite a opção desejada: '))
    n = resposta
    return n

# Função para cadastrar dados do agricultor e colocar esses dados em uma lista
def cadastroAgricultor():
    print("\n--- Cadastro do Agricultor ---\n")
    infoAgricultor = []
    nome = input('Digite seu nome completo: ')
    infoAgricultor.append(nome)
    email = input('Digite seu Email : ')
    infoAgricultor.append(email)
    cnpj = input('Digite seu CNPJ: ')
    infoAgricultor.append(cnpj)
    endereco = input('Digite o seu logradouro e numero: ')
    infoAgricultor.append(endereco)
    return infoAgricultor

# Função para cadastrar dados da secretaria de ensino e colocar esses dados em uma lista
def cadastroSecretaria():
    print("\n--- Cadastro da Secretaria ---\n")
    infoSecretaria = []
    nome = input('Digite o nome completo da secretaria: ')
    infoSecretaria.append(nome)
    email = input('Digite o Email : ')
    infoSecretaria.append(email)
    cnpj = input('Digite seu CNPJ: ')
    infoSecretaria.append(cnpj)
    endereco = input('Digite o seu logradouro e numero: ')
    infoSecretaria.append(endereco)
    return infoSecretaria

# Função para cadastrar os produtos que o agricultor vai disponibilizar
def cadastroProdutoAgro():
    print(" \n --- Cadastro dos produtos do Agricultor --- \n ")
    produtoAgro = []
    resposta = 1
    while resposta == 1:
        nome = input('Digite o Produto que deseja doar: ')
        produtoAgro.append(nome)
        tipo = input('Digite o tipo do produto doado (vegetal, carne, grão, fruta...): ')
        produtoAgro.append(tipo)
        quantidade = input('Digite a quantidade que deseja doar(Gramas, Kg, caixas, duzias...): ')
        produtoAgro.append(quantidade)
        resposta = int(input('Deseja Adicionar mais algum produto? \n [1] = Sim \n [2] = NÃO \n \n Resposta: '))
    return produtoAgro

# Função para cadastrar produtos solicitados pela secretaria
def cadastroProdutoSec():
    print("\n--- Cadastro dos produtos solicitados pela Secretaria ---\n")
    produtoSec = []
    resposta = 1
    while resposta == 1:
        nome = input('Digite o Produto que necessita receber: ')
        produtoSec.append(nome)
        tipo = input('Digite o tipo do produto requisitado (vegetal, carne, grão, fruta...): ')
        produtoSec.append(tipo)
        quantidade = input('Digite a quantidade que necessita receber (Gramas, Kg, caixas, duzias...): ')
        produtoSec.append(quantidade)
        resposta = int(input('Deseja adicionar mais um Produto? \n[1] SIM \n[2] NÃO \n Resposta: '))

    return produtoSec

# Função para imprimir quantidade, tipo e produto doado pelo agricultor e dados do agricultor
def imprimeAgro(infoAgro, produtoAgro):
    print('--------INFORMAÇÕES DO AGRICULTOR--------')
    print(f'Nome: {infoAgro[0]} \n Email: {infoAgro[1]} \n CNPJ: {infoAgro[2]} \n Endereço: {infoAgro[3]}')
    print('\n----------------PRODUTOS-----------------\n')
    for i in range(0, len(produtoAgro), 3):
        print(f'Nome: {produtoAgro[i]} \n Tipo: {produtoAgro[i+1]} \n Quantidade: {produtoAgro[i+2]} \n')

# Função para imprimir quantidade, tipo e produto solicitado pela secretaria
def imprimeSecre(infoSec, produtoSec):
    print('--------INFORMAÇÕES DA SECRETARIA--------')
    print(f'Nome: {infoSec[0]} \n Email: {infoSec[1]} \n CNPJ: {infoSec[2]} \n Endereço: {infoSec[3]}')
    print('\n----------------PRODUTOS-----------------\n')
    for i in range(0,len(produtoSec),3):
        print(f'Nome: {produtoSec[i]}\nTipo: {produtoSec[i+1]}\nQuantidade: {produtoSec[i+2]}\n')

# Função principal que chama as outras funções
def principal():
    resposta = menu()
    if resposta == 1:
        infAgri = cadastroAgricultor()
        prodAgri = cadastroProdutoAgro()
        imprimeAgro(infAgri, prodAgri)
    elif resposta == 2:
        infSec = cadastroSecretaria()
        prodSecr = cadastroProdutoSec()
        imprimeSecre(infSec,prodSecr)

# Chamando a função principal
principal()
