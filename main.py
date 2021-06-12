from bs4 import BeautifulSoup
import requests
import pyautogui
import time 

def spam(url, tag):
    time.sleep(5)
    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    html = parse.find_all(tag)
    print(html)

    for msg in html:
        pyautogui.typewrite(msg.get_text())
        pyautogui.press("enter")

spam('https://www.mundodasmensagens.com/mensagens-positividade/', 'p')
