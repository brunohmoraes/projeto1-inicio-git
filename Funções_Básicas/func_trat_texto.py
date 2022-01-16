produtos = ['  aBAcate', 'CEREJA', ' LAranja', 'peRA']

# texto = ' CEREJA'


def tratar_texto(texto):
    texto = texto.lower()
# upper() para deixar em maiusculo
# casefold() lower case

    texto = texto.strip()
# strip() remove os espaços do inicio e/ou fim do texto

    return texto


texto = ' CEREJA'

texto = tratar_texto(texto)

# print(texto)

for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)

print(produtos)
