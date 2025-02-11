from funcionalidades import *

arq = 'lista.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

titulo('LISTA DE COMPRAS MAKER', 42, '=-', verde)
while True:
    titulo('MENU', 42, '-', azul)
    print('1 - Adicionar itens na lista / 2 - Ver lista / 3 - Sair')
    resp = int(input('Sua escolha: '))
    match resp:
        case 1:
            item = str(input('Item: '))
            quant = int(input('Quantidade:'))
            adicionar_itens(arq, item, quant)
        case 2:
            ler_arquivo(arq)
        case 3:
            break
print('Lista Finalizada!')
titulo('VOLTE SEMPRE!', 42, '=-', verde)
