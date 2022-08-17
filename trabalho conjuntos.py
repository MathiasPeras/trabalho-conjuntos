# Matheus Gabriel Pereira Nogueira
'''
ENUNCIADO
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de
operações que serão realizadas entre dois conjuntos de dados.
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas
seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da
operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e
terceira linhas conterão os elementos dos conjuntos separados por virgulas.
'''

abr_arquivo = open('trabalho 1.txt')
arquivo = abr_arquivo.read()
lines = arquivo.split('\n')
linhas = []
for i in range(len(lines)):
    linhas.append(lines[i])
abr_arquivo.close()


def Resposta(result):

    resp = '{' + result[0]
    for i in range(1, len(result)):
        resp = f"{resp}, " + result[i]
    resp = f" {resp}"+ '}'

    return resp


def União(x, y):
    if y == 'U':
        linha1 = lines[x + 1]
        linha2 = lines[x + 2]
        sep_l1 = linha1.split(', ')
        sep_l2 = linha2.split(', ')
        for item in sep_l2:
            if item not in sep_l1:

                sep_l1.append(item)
        print(f"União: conjunto 1: {{{linha1}}}, conjunto 2: {{{linha2}}}. Resultado: {Resposta(sep_l1)}")


def Diferença(x, y):
    if y == 'D':

        linha1 = lines[x + 1]
        linha2 = lines[x + 2]
        sep_l1 = linha1.split(', ')
        sep_l2 = linha2.split(', ')
        resultado = []
        for item in sep_l1:
            if item not in sep_l2:
                resultado.append(item)
        print(f"Diferença: conjunto 1: {{{linha1}}}, conjunto 2: {{{linha2}}}. Resultado: {Resposta(resultado)}")


def Interseção(x, y):
    if y == 'I':
        linha1 = lines[x + 1]
        linha2 = lines[x + 2]
        sep_l1 = linha1.split(', ')
        sep_l2 = linha2.split(', ')
        resultado = []
        for i in range(len(sep_l1)):
            for o in range(len(sep_l2)):
                if sep_l2[o] == sep_l1[i]:
                    resultado.append(sep_l1[i])
        print(f"Interseção: conjunto 1: {{{linha1}}}, conjunto 2: {{{linha2}}}. Resultado: {Resposta(resultado)}")


def Prod_cartesiano(x, y):
    if y == 'C':
        linha1 = lines[x + 1]
        linha2 = lines[x + 2]
        sep_l1 = linha1.split(', ')
        sep_l2 = linha2.split(', ')
        resultado = []
        for i in range(len(sep_l1)):
            for o in range(len(sep_l2)):
                x = sep_l1[i] + '-' + sep_l2[o]
                resultado.append(x)
        print(f"Produto Cartesiano: conjunto 1: {{{linha1}}}, conjunto 2: {{{linha2}}}. Resultado: {Resposta(resultado)}")


num_op = int(linhas[0])
n = 1
for i in range(num_op):
    União(n, linhas[n])

    Diferença(n, linhas[n])

    Interseção(n, linhas[n])

    Prod_cartesiano(n, linhas[n])
    n += 3
