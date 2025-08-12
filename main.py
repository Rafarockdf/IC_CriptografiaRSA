from RSA_IC import RSA

rsa = RSA()

# transforma frase
numeros = rsa.pre_transforma_frase("PARATY É LINDA")
print(numeros)  # [25, 10, 27, 10, 29, 34, 14, 21, 23, 13, 13, 10]

# calcula chave
chave = rsa.pre_blocagem(11, 13)
print(chave)
