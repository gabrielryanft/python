from random import randint
while True:
    print("Examinador de listas. Esse examinador examina qual é o primeiro numero que mais se repete na lista.")
    while True:
        try:
            escolha = int(input("Você quer: \n -1- Criar uma lista; \n -2- Usar uma pronta. \n Resposta: "))

            if escolha not in [1, 2]:
                print("Só existem as opções 1 e 2. Escolha uma delas.")

            elif escolha == 1:
                while True:
                    try:
                        numero_itens = int(input("quantos itens a lista tera?"))

                        if numero_itens > 100 or numero_itens < 3:
                            print("A lista precisa ter no minimo 3 itens e no maximo 100.")
                            continue

                        lista = list()
                        while numero_itens > 0:
                            try: 
                                lista.append(int(input(f"{numero_itens}º item: ")))
                                numero_itens -= 1

                            except (TypeError, ValueError):
                                print("\033[1;37;41m[Valor invalido]\033[m A lista precisa ter somente números.")

                    except (TypeError, ValueError):
                        print("\033[1;37;41m[Valor invalido]\033[m Digite um número de 3 a 100")

                    break

            elif escolha == 2:
                lista = list()
                for i in range(0, 20):
                    lista.append(randint(0, 20))
                    

        except (TypeError, ValueError):
            print("\033[1;37;41m[Valor invalido]\033[m Escolha a opção 1 ou 2:")
            continue

        break

    num_mais_repete = max(set(lista), key=lista.count) #set() pega cada item individalmente // key=lista.count diz que o max deve retornar um resultado baseado no numero que mais se repete(count) ao inves de retornar o maior número.
    print(f"A lista usada foi: {lista}")
    print(f"O primeiro número que mais se repete é o {num_mais_repete}.")
    while True:
        try:
            continuar = str(input("Você quer continuar? (y / n) ")).strip().lower()
            if continuar not in "yn":
                print("Digite \"s\" (Sim) ou \"n\" (Não).")
                continue

            break

        except (TypeError, ValueError):
            print("\033[1;37;41m[Valor invalido]\033[m Digite \"s\" (Sim) ou \"n\" (Não).")
    
    if continuar not in "y":
                break
    
print("Tenha um bom dia")