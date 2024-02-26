from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.implicitly_wait(40)

navegador.get('https://chercher.tech/practice/implicit-wait-example') 
checkbox = navegador.find_element(By.XPATH, '//*[@id="q"]/input[4]')
assert checkbox.is_displayed()
print('passed!')

