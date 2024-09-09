import time

class escolhas:
    def __init__(self, jogo):
        if jogo in 'Nn':
            print('Foda-se!', end='')
        elif jogo not in 'Nn':
            print('Otimo!', end='')

        print(' Primeira  pergunta: ')
        time.sleep(0.3)

        print("Oque é que é? ")
        time.sleep(0.3)

        print(" -- Sim (Type 1 )")
        time.sleep(0.3)

        print(' -- Provavelmente não, mas tem uma possibilidade de ser sim:\nComo diria: "Tudo é tão provavel quanto qualquer outra coisa."\n - Rick, from rick and Morty.  (Type 2 ).')
        time.sleep(0.3)

        print(" -- Não (Type 3 )")
        time.sleep(0.3)

        resposta = int(input('Digite a sua resposta: '))

        if resposta == 2:
            print('   \033[35mSeu totosão! é isso mesmo! A resposta é 2!\033[m')
        elif resposta > 3 or resposta < 1:
            print(f"   \033[35m\"A resposta é {resposta}\"! Essa resposta não existe mas pode ser!!\033[m")
        else: print(f"   \033[35mNão bro, Não! Quem responderia \"{resposta}\"?! Tenha um bom dia!\033[m")


escolhas(input("Quer jogar? ( S / N ) "))