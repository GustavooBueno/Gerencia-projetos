import pyautogui
import time
import pyperclip
import pandas as pd

#Nome Mudado
#pyautogui.displayMousePosition()
pyautogui.PAUSE = 1

#Passo 1
#Abrir uma nova aba
time.sleep(2)
pyautogui.hotkey('ctrl', 't')
#Entrar no link do sistema
link = "https://shoesystems.bubbleapps.io/version-test?debug_mode=true"
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#Passo 2
time.sleep(7)
pyautogui.click(681, 409, clicks = 1)
time.sleep(2)

#Passo 3
pyautogui.click(659, 228, clicks = 1)
pyautogui.write('Gustavo')
pyautogui.press('tab')
pyautogui.write('gustavo@gmail.com')
pyautogui.press('tab')
pyautogui.write('19984287643')
pyautogui.press('tab')
pyautogui.write('123')
pyautogui.press('tab')
pyautogui.write('123')
pyautogui.press('tab')
pyautogui.write('12126438911')
pyautogui.press('tab')
pyautogui.write('Rua X')
pyautogui.press('enter')
data_nascimento = '07062002'
pyperclip.copy(data_nascimento)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
pyautogui.write('5592587815')
pyautogui.press('tab')

#Menu
pyautogui.click(677, 598
, clicks = 1)
time.sleep(2)
pyautogui.click(660, 472, clicks = 1)
pyautogui.press('tab')

#Comprar
time.sleep(3)
pyautogui.click(676, 543, clicks = 1)
time.sleep(4)
pyautogui.press('space')
time.sleep(4)
pyautogui.click(17, 47, clicks = 1) 

#Estoque
time.sleep(3)
pyautogui.click(667, 583, clicks = 1)
time.sleep(2)
pyautogui.click(669, 526, clicks = 1)
time.sleep(2)
pyautogui.click(628, 394, clicks = 1)
time.sleep(4)
pyautogui.press('space')
time.sleep(1)
pyautogui.click(17, 47, clicks = 1)

#Consultar Estoque
time.sleep(3)
pyautogui.click(631, 501, clicks = 1)
time.sleep(2)
pyautogui.press('space')
time.sleep(1)
pyautogui.click(17, 47, clicks = 1)

#Voltar
time.sleep(3)
pyautogui.click(17, 47, clicks = 1)
time.sleep(3)

#Fornecedor
pyautogui.click(679, 619, clicks = 1)
time.sleep(2)
pyautogui.click(670, 423, clicks = 1)
time.sleep(2)
pyautogui.press('space')
time.sleep(1)
pyautogui.click(17, 47, clicks = 1)

#Editar Fornecedor
time.sleep(3)
pyautogui.click(668, 480, clicks = 1)
time.sleep(2)
pyautogui.click(161, 129, clicks = 1)
time.sleep(3)

#Sou um funcionario
pyautogui.click(664, 478, clicks = 1)
time.sleep(3)
pyautogui.click(249, 449, clicks = 1)
time.sleep(3)
pyautogui.press('space')
time.sleep(1)
pyautogui.click(17, 47, clicks = 1)
time.sleep(3)

#cadastrar produto
pyautogui.click(663, 453, clicks = 1)
time.sleep(3)
pyautogui.press('space')
time.sleep(1)
pyautogui.click(17, 47, clicks = 1)
time.sleep(3)

#excluir produto
pyautogui.click(1074, 459, clicks = 1)
time.sleep(3)
pyautogui.press('space')
time.sleep(1)
pyautogui.click(17, 47, clicks = 1)
time.sleep(3)

#cadastrar e editar funcionario
pyautogui.click(183, 615, clicks = 1)
time.sleep(3)
pyautogui.click(287, 428, clicks = 1)
time.sleep(1)
pyautogui.click(441, 610, clicks = 1)
time.sleep(3)
pyautogui.click(17, 47, clicks = 1)
time.sleep(3)

#excluir funcionario
pyautogui.click(668, 607, clicks = 1)
time.sleep(3)
pyautogui.click(17, 47, clicks = 1)
time.sleep(3)

#consultar funcionario
pyautogui.click(925, 611, clicks = 1)
time.sleep(3)
pyautogui.click(17, 47, clicks = 1)
time.sleep(3)

#espaço
pyautogui.press('space')

#cadastar e editar cliente
pyautogui.click(187, 211, clicks = 1)
time.sleep(3)
pyautogui.click(187, 211, clicks = 1)
time.sleep(2)
pyautogui.click(432, 216, clicks = 1)
time.sleep(4)
pyautogui.click(17, 47, clicks = 1)
time.sleep(3)

#excluir cliente
pyautogui.click(678, 215, clicks = 1)
time.sleep(4)
pyautogui.click(169, 130, clicks = 1)
