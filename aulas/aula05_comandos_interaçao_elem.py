from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://www.saucedemo.com/v1/index.html')

navegador.find_element(By.ID, 'user-name').send_keys('standard_user')
navegador.find_element(By.ID, 'password').send_keys('secret_sauce')
navegador.find_element(By.XPATH, '//*[@class="btn_action"]').click()
sleep(2)

#text
title = navegador.find_element(By.CLASS_NAME, 'product_label')
assert title.text == 'Products'
print(title.text)

img_mochila = navegador.find_element(By.XPATH,'//img[@src="./img/sauce-backpack-1200x1500.jpg"]')
print(img_mochila.get_attribute('class'))
assert img_mochila.get_attribute('class') == 'inventory_item_img'
