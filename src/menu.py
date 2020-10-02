import asyncio
from funcoes import *


def menu():
    Menu = '''
------------------------------------------------------------------------------------
[1] - DADOS POR CIDADE        [2] - DADOS POR IDADE         [3] - DADO POR MESES 
[4] - DADOS POR DOENÇA        [5] - DADOS POR GÊNERO        [6] - DADOS EM CONJUTO
[7] - DADO GERAL ESTADUAL     [8] - SAIR
------------------------------------------------------------------------------------
    '''
    print(Menu)
    escolha = int(input('Escolha: '))
    
    if(escolha == 8):
        async def main():
            print('Finalizando...')
            await asyncio.sleep(2)
            print('...finalizado !')
        return asyncio.run(main())
    else:
        SubMenu(escolha)


def SubMenu(args):
    if args == 1:
        SubMenu ='''
------------------------------------------------------------------------------------
[1] - DADOS COMPLETOS / ESTATÍSTICO     [2] - DADOS POR IDADE
[3] - DADOS POR GÊNERO                  [4] - DADOS POR IDADE/GENÊRO
[5] - DADOS POR COMOBIDADES             [6] - DADOS POR IDADE/GENÊRO/COMORBIDADES
[7] - DADOS POR CASOS                   [8] - VOLTAR
------------------------------------------------------------------------------------
'''
    print(SubMenu)
    escolha = input('Escolha: ')
    if escolha == '1':
        tratarDado(city())
        retorno()
    elif escolha != '8':
        if escolha == '2':
            age = idade('2')
            retorno()
        elif  escolha =='3':
            gender('3')
            retorno()
        elif escolha == '4':
            gender('4')            
            retorno()


    else:
        return menu()

def retorno():
    print(84*'-')
    escolha = input('Deseja continuar? [1] - SIM , Qualquer outra tecla para não: ')
    if escolha == '1':
        return menu()
    else:
        async def main():
            print('Finalizando...')
            await asyncio.sleep(2)
            print('...finalizado !')
        return asyncio.run(main())
