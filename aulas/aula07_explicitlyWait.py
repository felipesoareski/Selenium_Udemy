from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from time import sleep

# Inicializa o driver do navegador (no caso, o Chrome)
navegador = webdriver.Chrome()

# Maximiza a janela do navegador
navegador.maximize_window()

# Abre a página web desejada
navegador.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')

# Cria uma espera explícita com um timeout de 20 segundos
wait = WebDriverWait(navegador, 20)

# Clica no botão que gera um alerta
navegador.find_element(By.ID, 'alert').click()

# Aguarda até que o alerta esteja presente e, em seguida, aceita o alerta
wait.until(ec.alert_is_present())
alerta = navegador.switch_to.alert
alerta.accept()

# Aguarda até que o texto 'Selenium Webdriver' esteja presente em um elemento específico
navegador.find_element(By.ID, 'populate-text').click()
wait.until(ec.text_to_be_present_in_element((By.CLASS_NAME, 'target-text'), 'Selenium Webdriver'))

# Obtém o texto do elemento e verifica se é igual a 'Selenium Webdriver'
target_text = navegador.find_element(By.CLASS_NAME, 'target-text').text
assert target_text == 'Selenium Webdriver'

# Clica no botão que exibe outro botão e espera até que ele esteja clicável
navegador.find_element(By.ID, 'display-other-button').click()
wait.until(ec.element_to_be_clickable((By.ID, 'hidden')))

# Clica no botão oculto
navegador.find_element(By.XPATH, '//*[@class="btn btn-primary btn-xs"]').click()

# Aguarda até que o elemento com ID 'ch' esteja selecionado
wait.until(ec.element_to_be_selected(navegador.find_element(By.ID, 'ch')))

# Fecha o navegador após a interação
navegador.quit()
