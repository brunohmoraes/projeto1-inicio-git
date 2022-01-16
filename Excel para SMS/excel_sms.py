import pandas as pd
from twilio.rest import Client

# Your Accond SID from twilio.com/console
account_sid = "AC941e4f055a1a6cdf85ce066374675c93"
# Ypur Auth Token from twilio.com/console
auto_token = "5b193d92dd9059edaa32aa7e68bd4861"

client = Client(account_sid, auto_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'C:\\Users\\bruno\\Projetos Python\\excel_to_sms\\{mes}.xlsx')
    condicao_teste = tabela_vendas['Vendas'] > 55000
    if (condicao_teste).any():
        vendedor = tabela_vendas.loc[condicao_teste, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[condicao_teste, 'Vendas'].values[0]
        print(
            f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511982443139",
            from_="+17156414840",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# Para cada arquivo:

# Verificar sem algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Enviar um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
