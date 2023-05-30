#Função menu para identificação do usuario
def menu():
    n = 0
    print('\n--- Menu ---\n')
    print('Bem Vindo ao Cadastro do EcoByte!! \n Escolha uma opção: \n 1 - Sou Agricultor \n 2 - Represento a Secretaria da Educação \n')
    resposta = int(input('\n Digite a opção desejada: '))
    n = resposta
    return n

#Função para cadastrar dados do agricultor e colocar esses dados em uma lista
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
#Função para cadastrar dados da secretaria de ensino e colocar esses dados em uma lista
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
#função para cadastrar osprodutos que o agricultor vai disponibilizar
def cadastroProdutoAgro():
    print("\n--- Cadastro dos produtos do Agricultor ---\n")
    n= 1
    produtoAgro = []
    while n == 1:
        nome = input('Digite o Produto que deseja doar: ')
        produtoAgro.append(nome)
        tipo = input('Digite o tipo do produto doado (vegetal, carne, grão, fruta...): ')
        produtoAgro.append(tipo)
        quantidade = input('Digite a quantidade que deseja doar(Gramas, Kg, caixas, duzias...): ')
        produtoAgro.append(quantidade)
        resposta = int(input('Deseja Adicionar mais algum produto? \n [1] = Sim \n [2] = NÃO \n \n Resposta: '))
        n = resposta
    return produtoAgro
#função para cadastrar produtos pedidos pela secretaria!
def cadastroProdutoSecre():
    print("\n--- Cadastro dos produtos solicitados pela Secretaria ---\n")
    n = 1
    produtoSecre = []
    while n == 1:
        nome = input('Digite o Produto que necessita receber: ')
        produtoSecre.append(nome)
        tipo = input('Digite o tipo do produto requisitado (vegetal, carne, grão, fruta...): ')
        produtoSecre.append(tipo)
        quantidade = input('Digite a quantidade que necessita receber (Gramas, Kg, caixas, duzias...): ')
        produtoSecre.append(quantidade)
        resposta = int(input('Deseja Adicionar mais algum produto? \n [1] = Sim \n [2] = NÃO \n \n Resposta: '))
        n = resposta
    return produtoSecre


#Função para imprimir quantidade, tipo e produto doado pelo agricultor e dados do agricultor
def imprimeAgro(infoAgro,produtoAgro):
    print('--------INFROMAÇÕES DO AGRICULTOR--------')
    print(f' Nome: {infoAgro[0]}\n Email: {infoAgro[1]}\n CNPJ: {infoAgro[2]}\n Endereço: {infoAgro[3]} ')
    print('\n----------------PRODUTOS-----------------\n')
    print(produtoAgro)
#Função para imprimir quantidade, tipo e produto requisitado pela secretaria e dados da secretaria
def imprimeSecre(infoSecretaria,produtoSecre):
    print('--------INFROMAÇÕES DA SECRETARIA--------')
    print(f' Nome: {infoSecretaria[0]} \n Email: {infoSecretaria[1]} \n CNPJ: {infoSecretaria[2]} \n Endereço: {infoSecretaria[3]} ')
    print('\n----------------PRODUTOS-----------------\n')
    print(produtoSecre)
    

### Principal

n = menu()
#Valida o tipo de usuário escolhido e mostra o respectivo formulário
if n == 1: 
    infAgr = cadastroAgricultor()
    cadAgr = cadastroProdutoAgro()
    imprimeAgro(infAgr,cadAgr)
elif n == 2:
    infSec = cadastroSecretaria()
    cadSec = cadastroProdutoSecre()
    imprimeSecre(infSec,cadSec)
else:
    print('----------------')
    print('Opção invalida, digite novamente!!!')
    print('---------------- \n\n')
    while n != 1 and n!=2:
        n = menu()