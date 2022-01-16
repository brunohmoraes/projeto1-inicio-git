nome = 'bruno'
host = 'gmail.com'

email = f'{nome}@{host}'
print(email)
# Só exibe o que ta no print mesmo

print(email[0])
# O colchetes + numero exibe a letra da exata posição

print(email.find('g'))
# O find exibe a posição do elemento selecionado

print(email[:5])
# O numero dentro do colchetes exibe o caracter, o ponto duplo exibe tudo antes daquela letra

posicao = email.find('@')

print(email[posicao+1:])
# Isso busca o servidor

cpf = '12345612312'
print('O CPF tem', len(cpf), 'digitos.')
# Len é usado para contar a quantidade de caracteres
# O virgula é usado nessa concatenação

print(nome.capitalize())
# Capitalize sempre deixa a primeira letra em maíusculo
# casefold, lower para deixar tudo em minusculo

print(email.count('o'))
# Conta a qtd de veses que repete o item

print(email.endswith('.com'))
# Validação lógica se termina com determinado valor

# email.isalnum() valida se são alfanuméricos, valida de forma lógica e retorna false caso tenha algum outro caractere
# email.isalpha() valida de forma lógica se é composto apenas por letras
# email.isnumeric() valida de forma lógica se é composto somente por números
# email.isdigit() e email.isdecimal() para validar decimais (quase nunca utlizado)

print(email.split('@'))
# Separa todo o texto no item inputado
# splitilines() separa ot exto de acordo com os "enters" do texto
# startswhith() Verifica se ot exto inicia ocm determinado texto
# strip() Retira caracteres indesejados. Ex: espaços extras no inicio e fim do texto
# title() Coloca a 1ª letra de cada palavra em maiúscula
# upper() COloca o texto todo em maiúscula
