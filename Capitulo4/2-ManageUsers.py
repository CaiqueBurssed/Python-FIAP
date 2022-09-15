from Capitulo4.Functions import *
usuarios = {}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":

    if opcao == "I":
        inserir(usuarios)

    if opcao == "L":
        print(usuarios)

    opcao = perguntar()

