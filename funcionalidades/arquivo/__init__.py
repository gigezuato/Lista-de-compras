import csv
import pandas as pd
from tabulate import tabulate
from funcionalidades.geral import laranja, vermelho

ext_csv = '.csv'
ext_xlsx = '.xlsx'


def criar_arquivo(nome_arquivo):
    """
        -> Cria um arquivo csv com a codificação UTF-8.
    :param nome_arquivo: nome que o arquivo terá.
    """
    try:
        # Abre e fecha o arquivo no modo de escrita com a codificação UTF-8
        with open(nome_arquivo, 'w', newline='', encoding="utf-8") as a:
            escritor = csv.writer(a)
            escritor.writerow(['Produto', 'Quantidade'])  # Escreve os cabeçalhos
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
            leitor = csv.reader(a, delimiter=',')
            lista = list(leitor)

        if len(lista) <= 1:  # Se o arquivo não tiver linhas ou somente a linha com os títulos
            print('A lista de compras está vazia.')
            return

        print(tabulate(lista, headers="firstrow", tablefmt="fancy_grid", showindex=range(1, len(lista))))

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
    :param nome_arquivo: Nome do arquivo CSV
    :param item: Nome do produto a ser adicionado
    :param qtde: Quantidade do produto a ser adicionado
    :return:
    """
    # Adicionando o novo item
    try:
        # Adiciona item com índice
        with open(nome_arquivo, "a", newline="", encoding="utf-8") as a:
            escritor = csv.writer(a, delimiter=',')
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
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as a:
            leitor = csv.reader(a, delimiter=',')
            linhas = list(leitor)
    except Exception as e:
        print(f'Erro ao ler o aquivo: {e}')

    # Verifica se o número da linha é válido
    if indice < 1 or indice > len(linhas) - 1:
        print(f'\033[{vermelho}mEsse índice não existe!\033[m')
        return

    # Remove a linha do índice passado pelo usuário
    del linhas[indice]

    # Reescreve as linhas e mostra a tabela atualizada
    try:
        with open(nome_arquivo, "w", newline="", encoding="utf-8") as a:
            escritor = csv.writer(a, delimiter=',')
            for i in range(len(linhas)):
                escritor.writerow(linhas[i])
    except Exception as e:
        print(f'Erro ao reescrever o arquivo: {e}')

    print(f'\033[{laranja}mItem removido com sucesso!\033[m')
    mostrar_tabela(nome_arquivo)


def salvar(nome_arquivo, ):
    """
        -> Salva o arquivo .csv em .xlsx
    :param nome_arquivo: nome do arquivo a ser convertido
    """
    try:
        df = pd.read_csv(nome_arquivo + ext_csv)
        df.to_excel(nome_arquivo + ext_xlsx, index=False, engine='openpyxl')
        print(f'\033[{laranja}mArquivo {nome_arquivo + ext_xlsx} salvo com sucesso!\033[m')
    except Exception as e:
        print(f'Erro ao salvar o arquivo: {e}')