# Função menu para identificação do usuário
def menu():
    n = 0
    print('\n\n----------- Menu -----------\n')
    print('Bem Vindo ao Cadastro do EcoByte!!\n \n Escolha uma opção: \n 1 - Sou Agricultor \n 2 - Represento a Secretaria da Educação \n')
    resposta = int(input('Digite a opção desejada: '))
    n = resposta
    return n

# Função para cadastrar dados do agricultor e colocar esses dados em uma lista
def cadastroAgricultor():
    print("\n\n --- Cadastro do Agricultor --- \n")
    infoAgricultor = []
    nome = input('\n Digite seu nome completo: ')
    infoAgricultor.append(nome)
    email = input('\n Digite seu Email : ')
    infoAgricultor.append(email)
    cnpj = input('\n Digite seu CNPJ: ')
    infoAgricultor.append(cnpj)
    endereco = input('\n Digite o seu logradouro e numero: ')
    infoAgricultor.append(endereco)
    return infoAgricultor

# Função para cadastrar dados da secretaria de ensino e colocar esses dados em uma lista
def cadastroSecretaria():
    print("\n\n --- Cadastro da Secretaria ---\n ")
    infoSecretaria = []
    nome = input('\n Digite o nome da secretaria: ')
    infoSecretaria.append(nome)
    email = input('\n Digite o Email : ')
    infoSecretaria.append(email)
    cnpj = input('\n Digite seu CNPJ: ')
    infoSecretaria.append(cnpj)
    endereco = input('\n Digite o seu logradouro e numero: ')
    infoSecretaria.append(endereco)
    return infoSecretaria

# Função para cadastrar os produtos que o agricultor vai disponibilizar
def cadastroProdutoAgro():
    print("\n\n --- Cadastro dos produtos do Agricultor --- \n ")
    produtoAgro = []
    resposta = 1
    while resposta == 1:
        nome = input('\n Digite o Produto que deseja doar: ')
        produtoAgro.append(nome)
        tipo = input('\n Digite o tipo do produto doado (vegetal, carne, grão, fruta...): ')
        produtoAgro.append(tipo)
        quantidade = input('\n Digite a quantidade que deseja doar(Gramas, Kg, caixas, duzias...): ')
        produtoAgro.append(quantidade)
        resposta = int(input('\n Deseja Adicionar mais algum produto? \n [1] = Sim \n [2] = NÃO \n \n Resposta: '))
    return produtoAgro

# Função para cadastrar produtos solicitados pela secretaria
def cadastroProdutoSec():
    print("\n\n--- Cadastro dos produtos solicitados pela Secretaria ---\n")
    produtoSec = []
    resposta = 1
    while resposta == 1:
        nome = input('\n Digite o Produto que necessita receber: ')
        produtoSec.append(nome)
        tipo = input('\n Digite o tipo do produto requisitado (vegetal, carne, grão, fruta...): ')
        produtoSec.append(tipo)
        quantidade = input('\n Digite a quantidade que necessita receber (Gramas, Kg, caixas, duzias...): ')
        produtoSec.append(quantidade)
        resposta = int(input('\n Deseja adicionar mais um Produto? \n[1] SIM \n[2] NÃO \n Resposta: '))

    return produtoSec
# Função para mostrar a simulaçao de Agricultores cadastrados 
def agricultores():
    agricultor = [
        ['João Silva', 'joao@email.com', '123456789', 'Rua A, 123 - SP'],
        ['Maria Santos', 'maria@example.com', '987654321', 'Avenida B, 456 - SP'],
        ['Pedro Souza', 'pedro@example.com', '456789123', 'Rua C, 789 - RJ'],
        ['Luciana Oliveira', 'luciana@example.com', '321654987', 'Avenida D, 987 - RJ']
    ]
    return agricultor
# Função para mostrar a simulaçao de produtos do Agricultor cadastrados 
def agricultoProdutos():
    agroProd = [
        ['João Silva', 'Banana', 'Fruta', '1000 unidades'],
        ['João Silva', 'Abacate', 'Fruta', '100 unidades'],
        ['Maria Santos', 'Tomate', 'Vegetal', '40 kg'],
        ['Pedro Souza', 'Alface', 'Vegetal', '300 unidades'],
        ['Luciana Oliveira', 'Acem', 'Carne', '22 kg']
    ]
    return agroProd
# Função para mostrar a simulaçao de Secretarias cadastradas 
def secretariasEnsino():
    secretarias = [
        ['Diretoria Regional de Educação Butantã ', 'smedrebutantaadm@sme.prefeitura.sp.gov.br', '123456789', 'Rua Padre Eugênio Lopes, 361 ,Vila Progredior, SP '],
        ['Diretoria Regional de Educação Campo Limpo', 'smedrecampolimpoadm@sme.prefeitura.sp.gov.br', '987654321', 'Av. João Dias, 3763 Jardim Santo Antônio - SP'],
        ['Diretoria Regional de Educação Capela do Socorro', 'smedrecapsocorroadm@sme.prefeitura.sp.gov.br', '456789123', 'Rua Monte Carlo, 25 Veleiros - SP'],
        ['Diretoria Regional de Educação Guaianases', 'smedreguaianasesadm@sme.prefeitura.sp.gov.br', '321654987', 'Rua Agapito Maluf, 58 - Vila Princesa Isabel - SP']
    ]
    return secretarias
# Função para mostrar a simulaçao de produtos da Secretaria cadastradas 
def secretariaProdutos():
    secreProd = [
        ['Diretoria Regional de Educação Butantã', 'Banana', 'Fruta', '400 unidades'],
        ['Diretoria Regional de Educação Butantã', 'Abacate', 'Fruta', '30 unidades'],
        ['Diretoria Regional de Educação Campo Limpo', 'Tomate', 'Vegetal', '15 kg'],
        ['Diretoria Regional de Educação Capela do Socorro', 'Alface', 'Vegetal', '200 unidades'],
        ['Diretoria Regional de Educação Guaianases', 'Acem', 'Carne', '20 kg ']
    ]
    return secreProd

# Função para imprimir quantidade, tipo e produto doado pelo agricultor e dados do agricultor
def imprimeAgro(infoAgro, produtoAgro):
    print('\n --------INFORMAÇÕES DO AGRICULTOR-------- \n')
    print(f'\n Nome: {infoAgro[0]} \n Email: {infoAgro[1]} \n CNPJ: {infoAgro[2]} \n Endereço: {infoAgro[3]}')
    print('\n ----------------PRODUTOS----------------- \n')
    for i in range(0, len(produtoAgro), 3):
        print(f'\n Nome: {produtoAgro[i]} \n Tipo: {produtoAgro[i+1]} \n Quantidade: {produtoAgro[i+2]} \n')

# Função para imprimir quantidade, tipo e produto solicitado pela secretaria
def imprimeSecre(infoSec, produtoSec):
    print('\n--------INFORMAÇÕES DA SECRETARIA--------\n')
    print(f'\n Nome: {infoSec[0]} \n Email: {infoSec[1]} \n CNPJ: {infoSec[2]} \n Endereço: {infoSec[3]}')
    print('\n----------------PRODUTOS-----------------\n')
    for i in range(0,len(produtoSec),3):
        print(f'\n Nome: {produtoSec[i]}\nTipo: {produtoSec[i+1]}\nQuantidade: {produtoSec[i+2]}\n')
        
# Função que imprime a simulaçao de Agricultores cadastrados e seus produtos
def imprimeAgricultores(agricultores):
    print('\n--------AGRICULTORES CADASTRADOS--------\n')
    for agricultor in agricultores:
        print(f'\n Nome: {agricultor[0]}\n Email: {agricultor[1]}\n CNPJ: {agricultor[2]}\n Endereço: {agricultor[3]}\n')

# Função que imprime a simulaçao de produtos cadastrados pelo Agricultor
def imprimeProdutos(agroProd):
    print('\n--------PRODUTOS DOS AGRICULTORES--------\n')
    for produto in agroProd:
        print(f'\n Agricultor: {produto[0]}\n Nome: {produto[1]}\n Tipo: {produto[2]}\n Quantidade: {produto[3]}\n')

# Função que imprime a simulaçao de Secretarias cadastradas
def imprimeSecretarias(secretarias):
    print('\n--------SECRETARIAS CADASTRADOS--------\n')
    for secretaria in secretarias:
        print(f'\n Nome: {secretaria[0]}\n Email: {secretaria[1]}\n CNPJ: {secretaria[2]}\n Endereço: {secretaria[3]}\n')

# Função que imprime a simulaçao de produtos cadastrados pela Secretaria
def imprimeSecProdutos(secreProd):
    print('\n--------PRODUTOS SOLICITADO PELAS SECRETARIAS--------\n')
    for produtos in secreProd:
        print(f'\n Secretaria: {produtos[0]}\n Nome: {produtos[1]}\n Tipo: {produtos[2]}\n Quantidade: {produtos[3]}\n')

# Função principal que chama as outras funções
def principal():
    print('\n ---------- EcoByte ---------- \n')
    print('\n Bem-Vindo ao EcoByte, um sitema revolucionario que liga Agricultores com a secretaria da educação!!','\n')
    r = int(input(' Deseja ver alguns participantes do Projeto EcoByte? \n [1] SIM \n [2] NÃO \n\n Resposta: '))
    
    if r == 1:
      agricultores_cadastrados = agricultores()
      produtos_agricultores = agricultoProdutos()
      secretarias_cadastradas = secretariasEnsino()
      produtos_secretarias = secretariaProdutos()

      imprimeAgricultores(agricultores_cadastrados)
      imprimeProdutos(produtos_agricultores)
      imprimeSecretarias(secretarias_cadastradas)
      imprimeSecProdutos(produtos_secretarias)
      r = int(input('\n \n Deseja participar do Projeto EcoByte? \n [1] SIM \n [2] NÃO \n\n Resposta: '))
      if r == 1:
        resposta = menu()
        if resposta == 1:
            infAgri = cadastroAgricultor()
            prodAgri = cadastroProdutoAgro()
            imprimeAgro(infAgri, prodAgri)
        elif resposta == 2:
            infSec = cadastroSecretaria()
            prodSecr = cadastroProdutoSec()
            imprimeSecre(infSec,prodSecr)
        else:
            print('\n \n Opção invalida!! Tente novamente!!')
            menu()
      elif r == 2:
          print('\n Poxa que pena *_* ')
      else: ('\n\n Sua Opçao esta invalida!! Vamos começar de novo!!')
      
    elif r == 2:
        r = int(input('\n \n Deseja participar do Projeto EcoByte? \n [1] SIM \n [2] NÃO \n\n Resposta: '))
        if r == 1:
          resposta = menu()
          if resposta == 1:
              infAgri = cadastroAgricultor()
              prodAgri = cadastroProdutoAgro()
              imprimeAgro(infAgri, prodAgri)
              print('\n \n----- CADASTRO EFETUADO COM SUCESSO!! -----\n\n')
          elif resposta == 2:
              infSec = cadastroSecretaria()
              prodSecr = cadastroProdutoSec()
              imprimeSecre(infSec,prodSecr)
              print('\n \n----- CADASTRO EFETUADO COM SUCESSO!! -----\n\n')
          else:
              print('Opção invalida!! Tente novamente!!')
              menu()
        elif r == 2:
          print('\n Poxa que pena *_* ')
        else: ('\n\n Sua Opçao esta invalida!! Vamos começar de novo!!')
    else:
        principal()
    print('\n \n A EcoByte Agradece pela Atenção!!')
    print('\n \n ---- PROGRAMA ENCERRADO ---- \n\n')
# Chamando a função principal
principal()
