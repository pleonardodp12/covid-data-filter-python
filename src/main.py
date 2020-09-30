arquivo = open('./files_data/obitos_detalhes_covid19_ma.csv', 'r', encoding='latin-1')

idades = []

def funcao(cidade):
  for linha in arquivo.readlines():
    pessoa = linha.split(';')
    if pessoa[3] == cidade:
      idade = pessoa[1].upper().split()
      if idade[1] == 'MESES':
        idade = int(idade[0])/12
      else:
        idade = int(idade[0])
      idades.append(idade)
  media = sum(idades)/len(idades)
  print(f'A média de idades dos obitos vitimas do covid é: {media:.2f}')
  print(f'A MAIOR IDADE das vitimas do covid é {max(idades)}')


#  0         1      2       3         4          5
#Genero - idade - data - cidade - raça/cor - comorbidades
cidades = []
def listCidades():
  for row in arquivo.readlines():
    dados = row.split(';')
    cidade = dados[3]
    if cidade not in cidades:
      cidades.append(cidade)
      cidades.sort()
  return print(cidades)

def date():
  for row in arquivo.readlines():
    dados = row.split(';')
    print(dados)

masculino = []
feminino = []
def separaGenero():
  for row in arquivo.readlines():
    dados = row.split(';')
    genero = dados[0]
    idade = dados[1]
    if genero == 'MASCULINO':
      masculino.append(idade)
    elif genero =='FEMININO':
      feminino.append(idade)
  print(f'Existe {len(masculino)} óbitos masculinos e {len(feminino)} Femininos e o lotal de {len(masculino+feminino)}')

semComorbidade = []
comComorbidade = []
comorbidades = []
#Qual o número de óbitos sem comorbidades?
def mortosSemComorbidades():
  for row in arquivo.readlines():
    dados = row.split(';')
    comorbidade = dados[5]
    #['HIPERTENSÃO ARTERIAL', 'CARDIOPATIA',
    # 'SEM COMORBIDADE', 'OBESIDADE',
    # 'DOENÇA RENAL CRÔNICA', 'DIABETES MELLITUS',
    # 'OUTROS', 'PNEUMOPATIA', 'NEUROLÓGICO',
    # 'ONCOLÓGICO', '-']
    if comorbidade not in comorbidades:
      comorbidades.append(comorbidade)
    if comorbidade == 'SEM COMORBIDADE':
      semComorbidade.append(comorbidade)
    else:
      comComorbidade.append(comorbidade);

  for i in comorbidades:
    print(f'{i} = {comComorbidade.count(f"{i}")}')
  print(f'Existe {len(comComorbidade)} óbitos com comorbidades no MA')
  print(f'Existe {len(semComorbidade)} óbitos sem comorbidades no MA')
  # print(f'HIPERTENSÃO ARTERIAL = {comComorbidade.count("HIPERTENSÃO ARTERIAL")}')
  # print(f'CARDIOPATIA = {comComorbidade.count("CARDIOPATIA")}')
  # print(f'0BESIDADE = {comComorbidade.count("OBESIDADE")}')
  # print(f'DOENÇA RENAL CRÔNICA = {comComorbidade.count("DOENÇA RENAL CRÔNICA")}')
  # print(f'DIABETES MELLITUS = {comComorbidade.count("DIABETES MELLITUS")}')
  # print(f'NEUROLÓGICO = {comComorbidade.count("NEUROLÓGICO")}')
  # print(f'ONCOLÓGICO = {comComorbidade.count("ONCOLÓGICO")}')
  # print(f'OUTROS = {comComorbidade.count("OUTROS")}')
  # print(f'- = {comComorbidade.count("-")}')


if __name__ == '__main__':
  #date()
  #funcao('COROATÁ')
  #listCidades()
  #separaGenero()
  mortosSemComorbidades()
  