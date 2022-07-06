import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1

#Abrir nova aba
time.sleep(2)
pyautogui.hotkey('ctrl', 't')

#Entrar no link
link = "http://127.0.0.1:5500/index.html#"
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#Home
time.sleep(4)

#Sobre
pyautogui.click(853, 117, clicks=1)
time.sleep(2)

#Produtos
pyautogui.click(922, 120, clicks=1)
time.sleep(3)

#Review
pyautogui.click(1001, 117, clicks=1)
time.sleep(1)

#Contato
pyautogui.click(1079, 117, clicks=1)
time.sleep(2)

#Controle
pyautogui.click(1246, 921, clicks=1)
time.sleep(2)

#Funcionario - cadastrar
pyautogui.click(153, 391, clicks=1)
time.sleep(2)
pyautogui.click(628, 328, clicks=1)
pyautogui.write('Gustavo Bueno')
pyautogui.press('tab')
pyautogui.write('gustavo@gmail.com')
pyautogui.press('tab')
pyautogui.write('43719356808')
pyautogui.press('tab')
pyautogui.write('559259784')
pyautogui.press('tab')
pyautogui.write('07/06/2002')
pyautogui.press('tab')
pyautogui.write('43719356808')
pyautogui.press('tab')
pyautogui.write('desenvolvedor')
pyautogui.press('tab')
pyautogui.write('2020008823')
pyautogui.press('tab')
pyautogui.write('19993626264')
pyautogui.press('tab')
pyautogui.write('Avenida BPS, 369')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.click(17, 54, clicks=1)

#Funcionario - editar
time.sleep(2)
pyautogui.click(334, 393, clicks=1)
time.sleep(2)
pyautogui.press('space')
time.sleep(1)
pyautogui.click(17, 54, clicks=1)


#Funcionario - consultar
time.sleep(2)
pyautogui.click(527, 393, clicks=1)
time.sleep(2)
pyautogui.click(17, 54, clicks=1)

#Funcionario - excluir
time.sleep(2)
pyautogui.click(729, 393, clicks=1)
time.sleep(1)
pyautogui.click(17, 54, clicks=1)


#Cliente - cadastrar
time.sleep(2)
pyautogui.click(132, 644, clicks=1)
time.sleep(2)
pyautogui.click(649, 426, clicks=1)
pyautogui.write('Gustavo Bueno')
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('tab')
pyautogui.write('gustavo@gmail.com')
pyautogui.press('tab')
pyautogui.write('43719356808')
pyautogui.press('tab')
pyautogui.write('559259784')
pyautogui.press('tab')
pyautogui.write('07/06/2002')
pyautogui.press('tab')
pyautogui.write('19993626264')
pyautogui.press('tab')
pyautogui.write('Avenida BPS, 369')
pyautogui.press('tab')
pyautogui.click(17, 54, clicks=1)

#Cliente - editar
time.sleep(2)
pyautogui.click(342, 634, clicks=1)
time.sleep(1)
pyautogui.press('space')
time.sleep(1)
pyautogui.click(17, 54, clicks=1)

#Cliente - excluir
time.sleep(2)
pyautogui.click(515, 642, clicks=1)
time.sleep(2)
pyautogui.click(17, 54, clicks=1)


#Produto - cadastrar
time.sleep(2)
pyautogui.click(128, 884, clicks=1)
time.sleep(3)
pyautogui.click(17, 54, clicks=1)

#Produto - editar
time.sleep(2)
pyautogui.click(318, 884, clicks=1)
time.sleep(3)
pyautogui.click(17, 54, clicks=1)

#Produto - excluir
time.sleep(2)
pyautogui.click(895, 884, clicks=1)
time.sleep(3)
pyautogui.click(17, 54, clicks=1)

#Estoque - cadastrar
time.sleep(2)
pyautogui.press('space')
pyautogui.click(117, 734, clicks=1)
time.sleep(2)
pyautogui.click(17, 54, clicks=1)

#Estoque - consultar
time.sleep(2)
pyautogui.click(349, 734, clicks=1)
time.sleep(2)
pyautogui.click(17, 54, clicks=1)

#Fornecedor - cadastrar
time.sleep(2)
pyautogui.click(115, 978, clicks=1)
time.sleep(2)
pyautogui.click(17, 54, clicks=1)

#Fornecedor - editar
time.sleep(2)
pyautogui.click(323, 979, clicks=1)
time.sleep(3)
pyautogui.click(17, 54, clicks=1)
time.sleep(1)
pyautogui.click(17, 54, clicks=1)
time.sleep(1)
pyautogui.click(931, 120, clicks=1)

