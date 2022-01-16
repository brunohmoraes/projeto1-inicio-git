from selenium import webdriver
import urllib
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd


navegador = webdriver.Chrome()
navegador.get('http://cloud.hidroview.com.br/relatorio-customizado/110')

time.sleep(5)

navegador.find_element_by_xpath(
    '//*[@id="email"]').send_keys('bruno.moraes@henkel.com')

navegador.find_element_by_xpath(
    '//*[@id="password"]').send_keys('Jarule10')

navegador.find_element_by_xpath(
    '//*[@id="root"]/div/div/div[2]/div[5]/form/div/div').click()

navegador.find_element_by_xpath('//*[@id="scroll-menu"]/a[10]/div').click()

time.sleep(3)

# navegador.execute('http://cloud.hidroview.com.br/relatorio-customizado')

# time.sleep(2)

navegador.find_element_by_xpath(
    '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/button').click()

time.sleep(2)

navegador.find_element_by_xpath(
    '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/button[19]/span[2]/span').click()
