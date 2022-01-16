from selenium import webdriver
import urllib
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

# importar os arquivos para a mesma pasta

contatos_df = pd.read_excel(
    'C:\\Users\\bruno\\Projetos Python\\auto_mens_whatsapp\\Enviar.xlsx')
# display(contatos_df)


navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')

# espera aparecer o elemento que tem id de "side"

while len(navegador.find_elements_by_id('side')) < 1:
    time.sleep(1)

# login feito no app

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, 'Pessoa']
    numero = contatos_df.loc[i, 'Número']
    texto = urllib.parse.quote('"Oi {pessoa}! {mensagem}')
    link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
    navegador.get(link)
    while len(navegador.find_elements_by_id('side')) < 1:
        time.sleep(1)

    navegador.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)

# Inspecionar elemento no campo digitado no whatsapp web e inspecionar, selecionar a linha e copiar o XPath
