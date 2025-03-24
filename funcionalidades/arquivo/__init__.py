import csv
import pandas as pd

from funcionalidades.geral import laranja, vermelho


def criar_arquivo(nome_arquivo):
    """
        -> Cria um arquivo csv com a codificação UTF-8.
    :param nome_arquivo: nome que o arquivo terá.
    """
    try:
        # Abre e fecha o arquivo no modo de escrita com a codificação UTF-8
        with open(nome_arquivo, 'w', newline='', encoding="utf-8") as a:
            escritor = csv.writer(a)
            escritor.writerow(['Índice', 'Produto', 'Qtde'])  # Escreve os cabeçalhos
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
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as a:
            linhas = a.readlines()  # Lê cada linha do arquivo retornando uma lista de strings

        if len(linhas) <= 1:  # Se o arquivo não tiver linhas ou somente a linha com os títulos
            print('A lista de compras está vazia.')
            return

        # Gerar uma tabela simples com o  conteúdo do arquivo
        tabela = pd.read_csv(nome_arquivo, delimiter=',', index_col=0,  encoding="utf-8")
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
        -> Adiciona o índice gerado automaticamente, o item e a quantidade, digitados pelo usuário, na lista.
    :param nome_arquivo: nome do arquivo onde será adicionado.
    :param item: item que será adicionado
    :param qtde: quantidade do item
    """
    # Adicionando o novo item
    try:
        # Abre e fecha o arquivo no modo append (adicionar) com codificação UTF-8
        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as a:
            escritor = csv.writer(a)  # Escrever no arquivo
            escritor.writerow([item, qtde])

            print(f'\033[{laranja}mItem "{item}" adicionado com sucesso!\033[m')
    except Exception as e:
        print(f'Erro ao adicionar item: {e}')


def excluir_item(nome_arquivo, indice):
    """
        -> Exclui do arquivo csv o item do índice informado pelo usuário.
    :param nome_arquivo: nome do arquivo que contém a lista
    :param indice: índice do item que será excluído
    """
    # Lê todas as linhas do arquivo
    with open(nome_arquivo, 'r', encoding='utf-8') as a:
        linhas = a.readlines()

    # Verifica se o número da linha é válido
    if indice < 1 or indice > len(linhas) - 1:
        print(f'\033[{vermelho}mEsse índice não existe!\033[m')
        return

    # Remove a linha do índice passado pelo usuário
    del linhas[indice]

    # Reescreve as linhas e mostra a tabela atualizada
    with open(nome_arquivo, 'w', encoding='utf-8') as a:
        a.writelines(linhas)
    print(f'\033[{laranja}mItem removido com sucesso!\033[m')
    mostrar_tabela(nome_arquivo)