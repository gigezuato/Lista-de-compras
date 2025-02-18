from funcionalidades.geral import *
from funcionalidades.arquivo import *

# Nome do arquivo de texto
arq = 'lista.txt'

if not arquivo_existe(arq):  # Se o arquivo não existir, ele é criado
    criar_arquivo(arq)

titulo('LISTA DE MATERIAIS ESCOLARES', 42, '=-', verde)
# Enquanto a opção Sair não for escolhida, o loop é executado
while True:
    titulo('MENU', 42, '-', azul)
    print(f'\033[{laranja}m1 - Adicionar itens na lista / 2 - Ver lista / 3 - Remover item / 4 - Sair\033[m')
    # Pede que o usuário digite uma opção até que ela seja válida (número inteiro e dentro das opções disponíveis)
    while True:
        resp = leia_int('>> Sua escolha: ')
        if resp in range(0, 5):
            break
        else:
            print('\033[0;31mDigite uma opção válida! [1, 2, 3 ou 4]\033[m')
    # Cada opção é um case diferente
    match resp:
        case 1:  # Adicionar itens
            while True:
                item = str(input('>> Item: ')).strip()
                quant = leia_int('>> Quantidade:')
                adicionar_itens(arq, item, quant)
                while True:
                    continua = str(input('>> Deseja adicionar mais itens? [S/N]: ')).upper().strip()[0]
                    if continua in 'SN':
                        break
                    print(f'\033[{vermelho}mDigite S - sim ou N - não!\033[m')
                if continua == 'N':
                    break
        case 2:  # Ver itens
            mostrar_tabela(arq)
        case 3:  # Remover itens
            indice_excluir = int(input('>> Digite o índice do item que deseja excluir: '))
            excluir_item(arq, indice_excluir)
        case 4:  # Sair
            break

print(f'\033[{laranja}mLista Finalizada!\033[m')
titulo('BOAS COMPRAS!', 42, '=-', verde)
