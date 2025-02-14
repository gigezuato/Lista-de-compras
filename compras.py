from funcionalidades import *
from funcionalidades.arquivo import *

# Nome do arquivo de texto
arq = 'lista.txt'

if not arquivo_existe(arq):  # Se o arquivo não existir, ele é criado
    criar_arquivo(arq)

titulo('LISTA DE COMPRAS MAKER', 42, '=-', verde)
# Enquanto a opção Sair não for escolhida, o loop é executado
while True:
    titulo('MENU', 42, '-', azul)
    print('1 - Adicionar itens na lista / 2 - Ver lista / 3 - Sair')
    # Pede que o usuário digite uma opção até que ela seja válida (número inteiro e dentro das opções disponíveis)
    while True:
        resp = leia_int('Sua escolha: ')
        if resp in range(0, 5):
            break
        else:
            print('\033[0;31mDigite uma opção válida! [1, 2 ou 3]\033[m')
    # Cada opção é um case diferente
    match resp:
        case 1:  # Adicionar itens
            while True:
                item = str(input('Item: '))
                quant = int(input('Quantidade:'))
                adicionar_itens(arq, item, quant)
                continua = str(input('Deseja adicionar mais itens? [S/N]: ')).upper().strip()[0]
                if continua == 'N':
                    break
        case 2:  # Ver itens
            ler_arquivo(arq)
        case 3:  # Sair
            break
print('Lista Finalizada!')
titulo('BOAS COMPRAS!', 42, '=-', verde)
