from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()
navegador.get('https://demo.applitools.com/')

username = navegador.find_element(By.ID, 'username')
checkbox = navegador.find_element(By.CLASS_NAME, 'form-check-input')

#is_displayed
print(f'is displayed: {username.is_displayed()}')
assert username.is_displayed()

#is_enabled
print(f'is enabled: {username.is_enabled()}')
assert username.is_enabled()

#clicando no checkbox
checkbox.click()
sleep(2)

#is_selected
print(f'is selected: {checkbox.is_selected()}')
assert checkbox.is_selected()
