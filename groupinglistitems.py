from itertools import groupby
from time import sleep
from random import randint, shuffle

def listaAleatoria(lista): 
    lista = ["girafa", "elefante", "zebra", "cabra", "beterraba", "carambolas", "entendo", "caramba", "belos Olhos", "foda-se", "carambola Fruta", "melão", "Arroz", "Maria feia", "beterraba", "terror", "Talentos", "America do Sul", "enriquecer", "Gabriel Totosão!"]
    numeroDItens = randint(9, 19)
    shuffle(lista)
    lista = lista[:numeroDItens]
    return lista

while True:
    lista = list()
    try:
        print("Escolha um: ")
        print(" 1 - Você cria uma lista; ")
        print(" 2 - Usar lista pronta.")
        resposta = int(input("Sua resposta: "))
    except (TypeError, ValueError):
        print("Valor inválido. tente de novo.")
        continue
    if resposta == 1:
        itemsNum = int(input("Número de itens da lista: "))
        for contador in range(1, itemsNum + 1):
            lista.append(input(f"Digite o {contador}° item da lista: "))
    elif resposta == 2:
        lista = listaAleatoria(lista)
    else:
        print("Resposta inválida. Usando lista pronta.")
        listaAleatoria(lista)

    print("\r Organizando lista", end="")
    sleep(0.5)
    print("\r Organizando lista.", end="")
    sleep(0.5)
    print("\r Organizando lista..", end="")
    sleep(0.5)
    print("\r Organizando lista...")
    sleep(0.5)

    lista.sort()
    listasAgrupadas = groupby(lista, key=lambda prim: prim[0])
    for chave, grupo in listasAgrupadas:
        print(chave, list(grupo)) # o grupo tem que estar dentro de uma list() porque ele é um bgl mt estranho (um objeto.) e o list() "traduz" isso.

    while True:
        continuar = str(input('Quer continuar? ( S / N ) '))
        if continuar in "SsNn":
            if continuar in "Nn":
                quit()
            else: break
        else:
            print("Resposta inválida. Tente de novo.")
            continue