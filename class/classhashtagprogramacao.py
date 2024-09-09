#Apredi a usar classes com o canal do youtube "hashtag programação".

class numerosClasse:
    def __init__(self, n1, n2):
        self.soma = n1 + n2

numeros_pessoa = numerosClasse(
    int(input('Digite um número: ')), 
    int(input('Digite outro número: '))
)
print(f"A soma dos números é : {numeros_pessoa.soma}!")