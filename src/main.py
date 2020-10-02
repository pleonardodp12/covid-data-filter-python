from menu import*

menu()





























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


def listData(select_gender ='MASCULINO', select_city='SÃO LUÍS', select_age=20):
  dados = obito_ma()
  genero = [genero for genero in dados if genero[0] ==select_gender]
  cidade = [cidade for cidade in dados if cidade[3] ==select_city]
  idade = [idade for idade in dados if idade[1] == select_age]
  comorbidades = [comorb for comorb in dados if 'SEM COMORBIDADE' in comorb ]
  return comorbidades

#b = input('Doença: ')
#a = len([numero for numero in dados if 'SEM COMORBIDADE' in numero])
a = listData()
print(len(a))

def verificadora():
  
  a = listData('FEMININO', 'SÃO LUÍS', 89)
     
  print(a[2])
 
verificadora()
'''

