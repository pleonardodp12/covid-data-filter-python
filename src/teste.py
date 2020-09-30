"""Abrindo os dados"""
dado_covid19 = open("./files_data/covid19_ma.csv", encoding="utf-8")
dado_obito_covid19 = open("./files_data/obitos_detalhes_covid19_ma.csv", encoding="latin-1")

"""Tranformando as informações por linhas em listas"""
dado_covid19 = dado_covid19.readlines()
dado_obito_covid19 = dado_obito_covid19.readlines()

""" Obtendo dados de casos por cidade"""
def case_c19_ma(*args):
    case_c19_ma = []
    for dados in args:
        dados = dados.split(',')
        case_c19_ma.append(dados)
    return case_c19_ma

""" Obtendo dados de óbitos"""
def obito_ma(*args):
    obito_ma = []
    for dados in args:
        dados = dados.split(";")
        idade = dados[1].split(" ")
        if idade[1] == "MESES":
            dados[1] = float(int(idade[0]) / 12)
        else:
            dados[1] = int(idade[0])
        while dados.count("-"):
            dados.remove("-")
        dados.pop()
        obito_ma.append(dados)
    return obito_ma

if __name__ == '__main__':
    case_c19_ma(*dado_covid19)
    
else:
    print('Tudo Bem !!!')

obitos  = obito_ma(*dado_obito_covid19)
'''
SEM COMORBIDADE
HIPERTENSÃO ARTERIAL
'''
b = input('Doença: ').upper()
a = len([numero for numero in obitos if b in numero])

print(a)