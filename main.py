from RSA_IC import RSA

rsa = RSA()
mensagem_codificada = rsa.codificar("Olá meu nome é rafael luiz")
print(f'Frase de Entrada = Paraty é linda')

# Acesse usando o nome interno gerado pelo Python
print(f'Chave Privada1 = {rsa._RSA__keyPrivate1}')
print(f'Chave Privada2 = {rsa._RSA__keyPrivate2}')
print(f'Chave Publica = {rsa._RSA__keyPublic}')

print(f'Mensagem Codificada = {mensagem_codificada}')
mensagem_decodificada = rsa.decodificar()
print(f'Mensagem Decodificada = {mensagem_decodificada}')

