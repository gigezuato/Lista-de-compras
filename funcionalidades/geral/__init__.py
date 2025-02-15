vermelho = '31'
roxo = '35'
azul = '36'
laranja = '34'
amarelo = '33'
verde = '32'
rosa = '31'
branco = '97'
preto = '30'
cinza = '37'


def titulo(msg, tam=42, simbolo='-', cor=vermelho):
    """
        -> Faz um título com o tamanho, símbolo e cor especificados.
    :param msg: o texto que será exibido como título.
    :param tam: tamanho do título - padrão: 42
    :param simbolo: símbolo que irá enfeitar o título - padrão: '-'
    :param cor: cor do título - padrão: vermelho - disponíveis: vermelho, roxo, azul, laranja, amarelo, verde, rosa,
    branco, preto e cinza.
    """
    print(f'\033[{cor}m{simbolo}\033[m' * tam)
    print(f'\033[{cor}m{msg.center(tam * len(simbolo))}\033[m')
    print(f'\033[{cor}m{simbolo}\033[m' * tam)


def leia_int(msg):
    """
        -> Só permite entrada de números inteiros.
    :param msg: mensagem exibida no input.
    :return: retorna o número inteiro digitado
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):  # Se der erro de valor ou de tipo
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue  # continuará perguntando para o usuário.
        else:
            return num