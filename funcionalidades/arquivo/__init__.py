import pandas as pd


def arquivo_existe(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'w', encoding="utf-8") as a:
            a.write('Índice,Produto,Qtde\n')
        print(f'Arquivo {nome_arquivo} criado com sucesso!')
    except Exception as e:
        print(f'Erro na criação do arquivo: {e}')


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        if len(linhas) <= 1:
            print('A lista de compras está vazia.')
            return

        tabela = pd.read_csv(nome_arquivo, delimiter=',', encoding="utf-8", index_col=0)
        print(tabela)

    except FileNotFoundError:
        print('Erro ao encontrar o arquivo!')
    except UnicodeDecodeError:
        print('Erro de codificação!')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')


def adicionar_itens(nome_arquivo, item, qtde):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        if len(linhas) > 1:
            ultimo_indice = int(linhas[-1].split(',')[0])
        else:
            ultimo_indice = 0
        novo_indice = ultimo_indice + 1

        with open(nome_arquivo, 'a', encoding='utf-8') as a:
            a.write(f'{novo_indice},{item},{qtde}\n')
            print(f'Item "{item}" adicionado com sucesso!')
    except Exception as e:
        print(f'Erro ao adicionar item: {e}')





