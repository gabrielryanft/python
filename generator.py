# generator

print("generetor\n")
print("generators can be USED only once.")
print("Ex.: sum(generetor); list(generetor) ...\n")

sq = (i * i for i in range(5))
print("sq = (i * i for i in range(5))\n")
print(type(sq))
print(sq, "\n")

print(" do this to transform the generator into a list: list(sq)\n")

print("do this to have the sum of all the items in the generator: sum(sq) \n")
print("do this to have the bigger of all the items in the generator: max(sq) \n")

print("print(next(sq))\n"*4)
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq), "\n")

print(list(sq), "\n")

print("""
for q in sq:
    print(q)
""")
for q in sq:
    print(q, "\n")

print(list(sq), "\n")

sq = [i * i for i in range(5)]
print("sq = [i * i for i in range(5)]\n")
print(type(sq), "\n")
print(sq, "\n")
