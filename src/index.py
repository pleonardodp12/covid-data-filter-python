from dados import obito_ma, case_c19_ma

#  0         1      2       3         4          5
# Genero - idade - data - cidade - raça/cor - comorbidades
'''
def genderMA(select_gender = 'MASCULINO'):
  dados = obito_ma()
  genero = [genero for genero in dados if genero[0] == select_gender]
  return genero

def cityMA(select_city = 'SÃO LUÍS',*args):
  dados = genderMA(*args)
  cidade = [cidade for cidade in dados if cidade[3] == select_city]
  return cidade

a = cityMA('ALTO ALEGRE DO MARANHÃO', 'FEMININO')
print(len(a))
'''


def listGender(select_gender ='MASCULINO', select_city='SÃO LUÍS', select_age=20):
  dados = obito_ma()
  genero = [genero for genero in dados if genero[0] ==select_gender]
  return genero

def listCity(select_city='SÃO LUÍS'):
  dados = obito_ma()
  cidade = [cidade for cidade in dados if cidade[3] ==select_city]
  
  
  return cidade

def listAge(select_age=20):
  dados = obito_ma()
  idade = [idade for idade in dados if idade[1] == select_age]
  return idade

def verificadora():
  city = listCity(input('Cidade: '))
  age = listAge(input('Idade: '))
  sexo = listGender(input('Sexo: '))
  
  coleta = []
  coleta.extend(city[3], age[1], sexo[0])
  return coleta

verificadora()
#listCity('SANTA INÊS')
  #a = listData('FEMININO', 'SÃO LUÍS', 89)
  
  # print(len(a[0]))
  # print(len(a[1]))
  
  
  # b =[]
  # for x in range(len(a[0])):
  #   for y in range(len(a[1])):
  #     if a[0][x] in a[1][y]:
  #       b.append(a[0])

    
  # print(b)

  #Feminio
  #São Lúis
  # 89
  #pergunta aqui os dados que queremos analisar
  #genero = input().upper()
  #cidade = input().upper()
  #analise = []
  #if genero == select_gender and cidade == select_city:
  #listTest.append(dados)
 

