meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
select_mes = input('Digite o mes: ').upper()

if len('leo') != 0:
  variavel = meses.index(select_mes.lower())
  print(f'não tivemos casos constatados no mês de {meses[variavel]} de 2020')
else:
  print('chegou')