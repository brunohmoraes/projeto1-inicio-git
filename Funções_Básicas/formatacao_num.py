faturamento = 1500000
custo = 500000
lucro = faturamento - custo

print(f'O lucro foi de R$ {lucro:,.2f}')
# O Python sempre usa ponto no lugar da vírgula
# Ele não coloca ponto em casa de milhar
# Após a variavel, usar dois pontos para iniciar a formatação do número
# A virgula adiciona o seperador de milhar
# Após os dois pontos .2f - Adiciona duas casas decimais em float
# O seperador de milhar sempre deve ir antes do decimal


margem = lucro / faturamento
print(f'A margem foi de {margem:.0%}')
# Adicionar a porcentagem no fim não transforma em float e forma ele em %

texto_lucro = f'R$ {lucro:_.2f}'
# O macete é no lugar da virgula usar o underline
texto_lucro = texto_lucro.replace('.', ',').replace('_', '.')
# O replace vc insere primeiro como é e depois muda para o que vc quer
print(f'O lucro foi de {texto_lucro}')
