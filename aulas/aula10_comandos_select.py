# Importa as bibliotecas necessárias do Selenium e time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# Inicializa o driver do navegador (no caso, o Chrome)
navegador = webdriver.Chrome()

# Abre a página web desejada
navegador.get('https://chercher.tech/practice/practice-dropdowns-selenium-webdriver')

# Localiza e interage com o primeiro dropdown selecionando 'Google' pelo texto visível
dropdown = Select(navegador.find_element(By.XPATH, '//select[@id="first"]'))
dropdown.select_by_visible_text('Google')

# Localiza e interage com o segundo dropdown selecionando 'big baby cat' pelo valor
# Em seguida, seleciona o terceiro item pelo índice após um intervalo de 2 segundos
dropdown_animals = Select(navegador.find_element(By.XPATH, '//select[@id="animals"]'))
dropdown_animals.select_by_value('big baby cat')
sleep(2)
dropdown_animals.select_by_index(3)
sleep(2)

# Localiza e interage com o terceiro dropdown selecionando 'Pizza' e 'Bonda' pelos textos visíveis
dropdown_food = Select(navegador.find_element(By.XPATH,'//select[@id="second"]'))
dropdown_food.select_by_visible_text('Pizza')
dropdown_food.select_by_visible_text('Bonda')

# Fecha o navegador após a interação
navegador.quit()
