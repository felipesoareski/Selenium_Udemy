from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://www.saucedemo.com/v1/index.html')

# find_element
# username = navegador.find_element(By.ID, 'user-name')
# password = navegador.find_element(By.ID, 'password')

# send_keys
# username.send_keys('standard_user')
# password.send_keys('secret_sauce')

# find_elements
aut_fields = navegador.find_elements(By.XPATH, '//*[@class ="form_input"]')
print(aut_fields)
print(len(aut_fields))
assert len(aut_fields) == 2

sleep(3)
