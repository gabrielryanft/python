# yield é semelhante ao generator.
# (Há um documento com esse nome que fala sobre esse assunto nesse repositório)

# Usando o yeld. BASICO.

def num_de_1a5():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


print(type(num_de_1a5))
# Retorna que é uma função.

# é necessário uma variável com o valor da função com a yield. se não não vai.
numero = num_de_1a5()

print(next(numero))
print(next(numero))
print(next(numero))
print(next(numero))
print(next(numero), "\n")

numero = num_de_1a5()
# tem que "reiniciar" a função

for n in numero:
    print(n)
