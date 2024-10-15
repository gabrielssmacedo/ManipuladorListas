from random import randint

def formata_lista(Lista, tamanho, digitos):
    """ Formata Lista como uma matriz bidimensional """

    print('\n'," " * (5 + digitos//2),'0', end='')
    for r in range(9):
        print(" " * (digitos+1) + str((r + 1)), end='')

    print(f'\n\n 00:  ', end='')
    for i in range(tamanho):
        if i > 0 and i % 10 == 0:
            print()
            if i < 100:
                print(f' {i}:  ', end='')
            else:
                print(f'{i}:  ', end='')
        k = 1
        menor = True
        while menor and k <= 10:
            if Lista[i] < 10**k:
                print(" " * (digitos - k), Lista[i],"", end="")
                menor = False
            k += 1
    print()

def remover_item(Lista, tamanho):
    """ Remove elemento fornecido pelo usuário """
    # Recebe o tamanho da Lista como argumento

    print("\nRemover item:\n  -Aleatório: 1\n  -Especifico: 2\n")

    remover = int(input('>> R: '))
    while remover != 1 and remover != 2:
        print("\nERRO: Funcionalidade Inexistente!")
        print("\nRemover item:\n  -Aleatório: 1\n  -Especifico: 2\n")
        remover = int(input('>> R: '))

    if remover == 1:
        posicao = randint(0,tamanho)
        deletado = Lista.pop(posicao)
        print(f'SUCESSO: Elemento {deletado} removido da posição {posicao}!\n')
        tamanho = len(Lista)
    else:
        posicao = int(input("Digite posição do elemento: "))
        deletado = Lista[posicao]
        del Lista[posicao]
        print(f'\nSUCESSO: Elemento {deletado} removido da posição {posicao}!\n')
        tamanho = len(Lista)
    return tamanho



def adicionar_item(resposta):
    """ Adiciona elemento aleatório ou específico na lista """
    # Recebe resposta como arg p/ selecionar o tipo de adição
    digitos = 0
    if resposta == 2:
        posicao = int(input('Inserir na posição: '))
        print("Escolha o intervalo do número aleatório:")
        Lmin = int(input("   Mínimo: "))
        Lmax = int(input("   Máximo: "))
        while Lmin > Lmax or Lmin < 0:
            print('\nERRO: Máximo deve ser MAIOR que o Mínimo e Mínimo >= 0!')
            Lmin = int(input("   Mínimo: "))
            Lmax = int(input("   Máximo: "))
        adicionar = randint(Lmin, Lmax)
        Lista.insert(posicao, adicionar)
        print(f'\nSUCESSO: elemento {adicionar} inserido na posição {posicao}!')
        digitos = len(str(adicionar))
    elif resposta == 3:
        especifico = int(input('Digite Número específico: '))
        posicao = int(input('Inserir na posição: '))
        Lista.insert(posicao, especifico)
        print(f'\nSUCESSO: elemento {especifico} inserido na posição {posicao}!')
        digitos = len(str(especifico))
    return digitos


def buscar_item(Indices, num):
    """ Procura elemento especificado pelo usuario """
    # Recebe lista Indices p/ as posições dos itens e elemento de procura como argumentos

    achou = False
    k = 0
    while k < Tamanho:
        if Lista[k] == num:
            achou = True
            Indices.append(k)
        k += 1
    return achou

def funcionalidade():
    """ Informa as opções p/ usuário, obtém e retorna sua resposta """
    print('\n\nFuncionalidades:')
    print('  - Remover item: 1')
    print('  - Adicionar aleatório: 2')
    print('  - Adicionar específico: 3')
    print('  - Busca: 4')
    print('  - Sair: 0')
    resposta = int(input('\n>> R: '))
    return resposta

#Main
print("\n"+"-"*65 + " Manipulador de Listas " + "-"*65)
print('\nDica: Para melhor visualização, expanda a Janela')
print("\nCrie sua Lista de maneira aleatória:")

Lista = []
Tamanho = int(input("\ntamanho da Lista: "))

print('\nVamos definir o intervalo dos números aleatórios que serão gerados:')
LMin = int(input("   Mínimo: "))
LMax = int(input("   Máximo: "))
while LMin > LMax or LMin < 0:
    print('\nERRO: Máximo deve ser MAIOR que o Mínimo e Mínimo >= 0!')
    LMin = int(input("   Mínimo: "))
    LMax = int(input("   Máximo: "))

TMax = str(LMax)
Digitos = len(TMax)

for i in range(Tamanho):
    N = randint(LMin, LMax)
    Lista.append(N)

print("\nLista gerada:")
formata_lista(Lista, Tamanho, Digitos)

Resposta = funcionalidade()

while Resposta != 1 and Resposta != 2 and Resposta != 3 and Resposta != 4:
    print("\nERRO: Funcionalidade Inexistente!")
    Resposta = funcionalidade()

while Resposta != 0:
    if Resposta == 1:
        Tamanho = remover_item(Lista, Tamanho)
        Digitos = len(str(max(Lista)))
        formata_lista(Lista, Tamanho, Digitos)
    elif Resposta == 2:
        DigMaiorList = len(str(max(Lista)))
        Inserido = adicionar_item(Resposta)
        if Inserido > DigMaiorList:
            Digitos = Inserido
        Tamanho = len(Lista)
        formata_lista(Lista, Tamanho, Digitos)
    elif Resposta == 3:
        DigMaiorList = len(str(max(Lista)))
        Inserido = adicionar_item(Resposta)
        if Inserido > DigMaiorList:
            Digitos = Inserido
        Tamanho = len(Lista)
        formata_lista(Lista, Tamanho, Digitos)

    else:
        Indices = []
        Busca = int(input("Procurar: "))
        Achou = buscar_item(Indices, Busca)
        if Achou:
            print(f'\nSUCESSO: Elemento {Busca} encontrado no(s) indice(s):')
            for p in Indices:
                print(p, end='  ')
        else:
            print(f'\nElemento {Busca} não encontrado!')
    Resposta = funcionalidade()


print('\n\nFim do Programa')


