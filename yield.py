# Usando o yeld. BASICO.

def num_de_1a5():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numero = num_de_1a5() #é necessário uma variável com o valor da função com a yield. se não não vai.

print(next(numero))
print(next(numero))
print(next(numero))
print(next(numero))
print(next(numero))