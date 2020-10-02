from dados import *

def tratarDado(dados):
    print(20*'-')
    print(f'Quantidade de óbitos na cidade: {len(dados)}')
    #Por gênero
    print(20*'-')
    print(f'Casos por gênero:')
    masc = 0; femin =0;
    for x in dados: 
        masc +=1 if x[0] == 'MASCULINO' else 0
        femin +=1 if x[0] == 'FEMININO' else 0
    try:
        print(f'Quantidade homens: {masc}')
        print(f'Quantidade mulheres: {femin}')
        print(f'Por proporção de casos, homens: {(masc/len(dados))*100 :.2f} %')
        print(f'Por proporção de casos, mulheres: {(femin/len(dados))*100 :.2f} %')
        print(20*'-')
        print('Comorbidades totais: ')
    except:
        print('CASO TODOS OS VALORES ESTEJAM ZERADOS, O NOME PODE ESTÁ ERRADO OU NÃO POSSUI ÓBITOS NA CIDADE DEVIDO A COVID19')
    #Quantidade por doenças
    comorbidades= []
    for x in dados:
        comorbidades.extend(x[5:])
    lista_doenca =  {element: 0 for element in comorbidades if element != ''}
    for x in comorbidades:
        if x in lista_doenca.keys():
            lista_doenca[x] += 1
    
    for index, valor in lista_doenca.items():
        print(f'{index.title()}: {valor} caso(s)')



#----------------------


def idade_estado(args):
    dados = obito_ma()
    drop_menu = '''
    Digite: 
    [1] - Idade por intervalo
    [2 ou outro valor] - Idade específica
    '''
    print(drop_menu)
    escolha = int(input('Escolha: '))
    if escolha == 1:
        text = '''
Digite dois valores, o primeiro é a idade inicial e o segundo será:
[Digite 1] - para ser maior ou igual a idade inicial
[Digite 2] - para ser menor do que a idade inicial'''   
        print(text)
        intervalo = (input('Digite o intervalo separado por espaço " ": \t')).split()
        intervalo = list(map(int, intervalo))
        if intervalo[1] == 1:
            age = [age for age in dados if age[1] >= intervalo[0] ]
            if args == '2':
                 return age_ret(age) 
            return age
        else:
            age = [age for age in dados if age[1] <= intervalo[0]]
            if args == '2':
                 return age_ret(age) 
            return age
    else:
        intervalo = int(input('Digite a idade: '))
        age = [age for age in dados if intervalo == age[1]]   
        if args == '2':
                 return age_ret(age) 
        return age
# Função para simplicar a saida de dados   
def age_ret(args):
    if len(args) >0:
        for x in args:
            print(f'Sexo: {x[0]}; Idade: {x[1]}; Data obito: {x[2]}; Cidade: {x[3]}; Comorbidades: {", ".join(x[5:])}')
        print(20*'-')
        print(f'Total de pessoas {len(args)}')
    else:
        print('Não possui dados para o valor informado') 

#--------------------------------------------------------------------------------

def gender_estado(args):
    def gender_dados(dados):
        select_gender = input('Digite o gênero: ').upper()
        genero = [genero for genero in dados if genero[0] == select_gender]
        return genero

    if args == '3':
        dados = obito_ma()
        age_ret(gender_dados(dados))

    elif args == '4' or '6':
        dados = idade('4')
        if args == '4':
            return age_ret(gender_dados(dados))
        return gender_dados(dados)
    
def comorbidades_estado(args):
    def comorbid(dados, args):
        comor = []
        for x in dados:
            comor.extend(x[5:])
        comor_entrada = input('Digite o nome da comorbidade: ')
        comorbidades = [comorb for comorb in dados if comor_entrada in comorb ]
        if args == '4':
            return age_ret(comorbidades)
        return comorbidades

    if args == '4':
        comorbid(obito_ma(), '4')
        
    elif args == '6':
        print(comorbid(gender('6'),'6'))


def datetimeSearch(args):
    def searchMouth(dados, args):
        meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
        select_mes = input('Digite o mes: ').upper()
        mes = [mes for mes in dados if mes[2].split('/')[1] == select_mes]
        # if select_mes == meses[0:2]: #'janeiro'or 'fevereiro'
        #     return print('não tivemos casos constatados no mês de janeiro e fevereiro de 2020')
        # elif select_mes == meses[9:11]: #'outubro' or 'novembro' or 'dezembro'
        #     return print('Meses com casos ainda não registrados')
        # else:
        #     return print(f'Tivemos {len(mes)} casos registrado no mês')
        
        print(f'Tivemos essa quantidade de óbitos: {len(mes)}, no mês {select_mes}')
        print(f'Mês 4 é: {meses[4]}')
        return mes

    if args == '5':
        print(searchMouth(obito_ma(),'5'))