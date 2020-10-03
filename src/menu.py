import asyncio
from funcoes_cidade import *
from funcoes_estado import *


def menu():
    Menu = """
------------------------------------------------------------------------------------
[1] - DADOS POR CIDADE        [2] - DADO GERAL ESTADUAL
[3] - SAIR
------------------------------------------------------------------------------------
    """
    print(Menu)
    escolha = int(input("Escolha: "))

    if escolha == 3:
        async def main():
            print("Finalizando...")
            await asyncio.sleep(2)
            print("...finalizado !")

        return asyncio.run(main())
    else:
        SubMenu(escolha)


def SubMenu(args):
    if args == 1:
        SubMenu1 = """
------------------------------------------------------------------------------------
[1] - DADOS COMPLETOS / ESTATÍSTICO     [2] - DADOS POR IDADE
[3] - DADOS POR GÊNERO                  [4] - DADOS POR IDADE/GENÊRO
[5] - DADOS POR COMOBIDADES             [6] - DADOS POR IDADE/GENÊRO/COMORBIDADES
[7] - DADOS POR MESES                   [8] - VOLTAR
------------------------------------------------------------------------------------
"""
        print(SubMenu1)
        escolha = input("Escolha: ")
        if escolha == "1":
            tratarDado(city())
            retorno()
        elif escolha != "8":
            if escolha == "2":
                age = idade("2")
                retorno()
            elif escolha == "3":
                gender("3")
                retorno()
            elif escolha == "4":
                gender("4")
                retorno()
            elif escolha == "5":
                comorbidades("5")
                retorno()
            elif escolha == "6":
                comorbidades("6")
                retorno()
            elif escolha == "7":
                meses("7")
                retorno()
        else:
            return menu()
    if args == 2:
        SubMenu2 = """
        
------------------------------------------------------------------------------------
[1] - DADO GERAL ESTADUAL     [2] - DADOS POR IDADE       [3] - DADOS POR GÊNERO 
[4] - DADOS POR COMOBIDADES   [5] - DADO POR MESES        [6] - DADOS EM CONJUTO
[8] - SAIR
------------------------------------------------------------------------------------
    """
        print(SubMenu2)
        escolha = input("Escolha: ")
        if escolha == '1':
            tratarDado(obito_ma())
            retorno()
        elif escolha != "8":
            if escolha == "2":
                age = idade_estado("2")
                retorno()
            elif escolha == "3":
                gender_estado("3")
                retorno()
            elif escolha == "4":
                comorbidades_estado("4")
                retorno()
            elif escolha == "5":
                datetimeSearch("5")
                retorno()
            elif escolha == "6":
                pass
            elif escolha == "7":
                pass
        else:
            return menu()
        """aqui mesma lógica do de cima"""


def retorno():
    print(84 * "-")
    escolha = input("Deseja continuar? [1] - SIM , Qualquer outra tecla para não: ")
    if escolha == "1":
        return menu()
    else:

        async def main():
            print("Finalizando...")
            await asyncio.sleep(2)
            print("...orbigado por esperar!")

        return asyncio.run(main())
