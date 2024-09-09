with open('c:caminho/para/o/doc', 'r') as minusculo, open('c:caminho/para/salvar/o/doc', 'w') as maiusculoCompleto:
    texto = minusculo.read()
    textoMaiusculo = texto.upper()
    maiusculoCompleto.write(textoMaiusculo)