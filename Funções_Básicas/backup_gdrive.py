import pyautogui
import time

pyautogui.alert(
    'O código vai começar. Não use o seu computador enquando o código está sendo rodado')
pyautogui.PAUSE = 1
# abrir o google drive

pyautogui.press('winleft')

pyautogui.write('python')

pyautogui.press('enter')

pyautogui.press('winleft')

pyautogui.write('chorome')

pyautogui.press('enter')

time.sleep(2)

pyautogui.write(
    'https://drive.google.com/drive/folders/13eO2Xqcflj3NkhF_3GPfevvD7T51CJfk')

pyautogui.press('enter')

# Entrar na área de trabalho

pyautogui.hotkey('alt', 'tab')

# pyautogui.position()
# Essa função digitada no terminal vai exibir o exato posicionamento do mouse no momento

# Cliquei no arquivo que quero fazer backup e arrastai ele

pyautogui.moveTo(621, 651)
pyautogui.mouseDown()

# Enquanto estou arrastado, vou mudar de tela para o google drive

# larguei no google driver

pyautogui.moveTo(1641, 351)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.mouseUp()

# esperar 5 segundos
time.sleep(5)

pyautogui.alert(
    'O código acabou de rodar. Pode usar o seu computador novamente')
