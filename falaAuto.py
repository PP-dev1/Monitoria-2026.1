import pyautogui
import pyperclip

mensagem = 'Galera, subi todos os códigos da monitoria no github, segue o link.'
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
pyautogui.press('enter')
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')


