from funcionalidades import *
from funcionalidades.arquivo import *

arq = 'lista.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

titulo('LISTA DE COMPRAS MAKER', 42, '=-', verde)
while True:
    titulo('MENU', 42, '-', azul)
    print('1 - Adicionar itens na lista / 2 - Ver lista / 3 - Sair')
    while True:
        resp = leia_int('Sua escolha: ')
        if resp in range(0, 5):
            break
        else:
            print('\033[0;31mDigite uma opção válida! [1, 2 ou 3]\033[m')
    match resp:
        case 1:
            while True:
                item = str(input('Item: '))
                quant = int(input('Quantidade:'))
                adicionar_itens(arq, item, quant)
                continua = str(input('Deseja adicionar mais itens? [S/N]: ')).upper().strip()[0]
                if continua == 'N':
                    break
        case 2:
            ler_arquivo(arq)
        case 3:
            break
print('Lista Finalizada!')
titulo('VOLTE SEMPRE!', 42, '=-', verde)
