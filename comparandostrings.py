# nesse documento py eu usei as funções enumerate() e zip(), que eu conhaci no canal "hashtag da programacao". (no Youtube, Tiktok e outras redes sociais.)

while True:
    try:
        escolha = int(input(
            "Você quer: \n -1- Comparar duas listas já existentes; \n -2- Fazer duas listas para comparar. \n Resposta: "))

        if escolha not in [1, 2]:
            print("Escolha o número 1 ou 2.")
            continue

        elif escolha == 1:
            str1 = "agora é hora de fazer coco sem o celular na mão."
            str2 = "agora é hora de fazer côco sem o celular na mão."

        elif escolha == 2:
            str1 = input("Digite a primeira lista de caracteres: ")
            str2 = input("Digite a segunda lista de caracteres: ")

        print(f"As listas usadas foram: \n - \"{str1}\"; \n - \"{str2}\".")

        lista_diferenca = enumerate(zip(str1, str2))
        itens_errados = 0
        for i, (a, b) in lista_diferenca:
            if a != b:
                print(f"Item errado: posição:{i} = ({a}, {b}).")
                itens_errados += 1

        plural = "s" if itens_errados > 1 else ""
        plural_itens = "ns" if itens_errados > 1 else "m"
        print("Não há nem um item errado na lista.") if itens_errados == 0 else print(
            f"Há {itens_errados} ite{plural} errado{plural} na lista.")

        while True:
            try:
                continuar = input(
                    "Você quer continuar? (y / n) ").strip().lower()
                if continuar not in "yn":
                    print("por favor, digite y ou n.")
                    continue

                break

            except (TypeError, ValueError):
                print(
                    "\033[1;37;41m[Valor invalido]\033[m Digite \"y\" (yes) ou \"n\" (Não).")

        if continuar in "y":
            continue

        break

    except (TypeError, ValueError):
        print("\033[1;37;41m[Valor invalido]\033[m Digite o número 1 ou 2.")

print("Tenha um bom dia.")
