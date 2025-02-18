import pandas as pd

from funcionalidades.geral import laranja, vermelho


def arquivo_existe(nome_arquivo):
    """
        -> Verifica se o arquivo txt já existe ou não.
    :param nome_arquivo: nome do arquivo que será verificado
    :return: retorna True se o arquivo existir e False se não existir.
    """
    try:
        a = open(nome_arquivo, 'rt')  # Abre o arquivo no modo de leitura
        a.close()  # Fecha o arquivo
    except FileNotFoundError:  # Erro ao encontrar o arquivo
        return False
    else:
        return True


def criar_arquivo(nome_arquivo):
    """
        -> Cria um arquivo txt com a codificação UTF-8.
    :param nome_arquivo: nome que o arquivo terá.
    """
    try:
        # Abre e fecha o arquivo no modo de escrita com a codificação UTF-8
        with open(nome_arquivo, 'w', encoding="utf-8") as a:
            a.write('Produto,Qtde\n')  # Assim que o arquivo é criado, escreve nele os títulos
        print(f'Arquivo {nome_arquivo} criado com sucesso!')

    except Exception as e:
        print(f'Erro na criação do arquivo: {e}')


def mostrar_tabela(nome_arquivo):
    """
        -> Faz a leitura do arquivo e mostra uma tabela simples com os dados.
    :param nome_arquivo: nome do arquivo que será lido.
    """
    try:
        # Abre e fecha o arquivo em modo de leitura com codificação UTF-8
        with open(nome_arquivo, 'r', encoding='utf-8') as a:
            linhas = a.readlines()  # Lê cada linha do arquivo retornando uma lista de strings

        if len(linhas) <= 1:  # Se o arquivo não tiver linhas ou somente a linha com os títulos
            print('A lista de compras está vazia.')
            return

        # Gerar uma tabela simples com o  conteúdo do arquivo
        tabela = pd.read_csv(nome_arquivo, delimiter=',', encoding="utf-8")
        tabela.index = tabela.index + 1  # Os índices começam a partir de 1
        print(tabela)

    # Possíveis erros
    except FileNotFoundError:
        print('Erro ao encontrar o arquivo!')
    except UnicodeDecodeError:
        print('Erro de codificação!')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')


def adicionar_itens(nome_arquivo, item, qtde):
    """
        -> Adiciona o item e a quantidade, digitados pelo usuário, na lista.
    :param nome_arquivo: nome do arquivo onde será adicionado.
    :param item: item que será adicionado
    :param qtde: quantidade do item
    """
    try:
        # Abre e fecha o arquivo no modo de leitura com codificação UTF-8
        '''with open(nome_arquivo, 'r', encoding='utf-8') as a:
            linhas = a.readlines()'''

        # Abre e fecha o arquivo no modo append (adicionar) com codificação UTF-8
        with open(nome_arquivo, 'a', encoding='utf-8') as a:
            a.write(f'{item},{qtde}\n')  # Escreve no arquivo o item e a quantidade
            print(f'\033[{laranja}mItem "{item}" adicionado com sucesso!\033[m')

    except Exception as e:
        print(f'Erro ao adicionar item: {e}')


def excluir_item(nome_arquivo, indice):
    """
        -> Exclui do arquivo txt o item do índice informado pelo usuário.
    :param nome_arquivo: nome do arquivo que contém a lista
    :param indice: índice do item que será excluído
    """
    # Lê todas as linhas do arquivo
    with open(nome_arquivo, 'r', encoding='utf-8') as a:
        linhas = a.readlines()

    # Verifica se o número da linha é válido
    if indice < 1 or indice > len(linhas):
        print(f'\033[{vermelho}mEsse índice não existe!\033[m')
        return

    # Remove a linha do índice passado pelo usuário
    del linhas[indice]

    # Reescreve as linhas e mostra a tabela atualizada
    with open(nome_arquivo, 'w', encoding='utf-8') as a:
        a.writelines(linhas)
    print(f'\033[{laranja}mItem removido com sucesso!\033[m')
    mostrar_tabela(nome_arquivo)