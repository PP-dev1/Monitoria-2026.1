import pyautogui
import pyperclip



mensagem = ('Galera, todos os códigos da monitoria e da atividade de while estão no github'
            ', deixei a 7 e a 8 comentadas para melhor entendimento')
link = 'https://github.com/PP-dev1/Monitoria-2026.1.git'
pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('whatsapp')
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.click(x=251, y=128)
pyautogui.write('P1 BCC')
pyautogui.press('enter')
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.write(': ')
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')


