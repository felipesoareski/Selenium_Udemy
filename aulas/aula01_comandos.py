from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()
navegador.get('https://www.google.com/')
navegador.get('https://www.saucedemo.com/v1/')

#maximixe window
navegador.maximize_window()
sleep(2)

#refresh
navegador.refresh()
sleep(2)

#back
navegador.back()
sleep(2)

#volta pra frente
navegador.forward()
sleep(2)

#abrir nova aba
navegador.switch_to.new_window('tab')
sleep(2)

#fecha aba
#navegador.close()

#quit()
navegador.switch_to.new_window('tab')
navegador.switch_to.new_window('tab')
navegador.switch_to.new_window('tab')
sleep(3)
navegador.quit()
