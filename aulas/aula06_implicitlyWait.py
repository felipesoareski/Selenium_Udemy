#time.sleep()
#implicitly.wait
#explicitly.wait

from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa o driver do navegador (no caso, o Chrome)
browser = webdriver.Chrome()

# Define um tempo de espera implícito de 12 segundos
browser.implicitly_wait(12)

# Abre a página web desejada
browser.get('https://chercher.tech/practice/implicit-wait-example')

# Localiza o elemento checkbox na página usando XPath
checkbox = browser.find_element(By.XPATH, '//*[@type="checkbox"]')

# Verifica se o checkbox está visível na tela
assert checkbox.is_displayed()
print('checkbox está na tela')

# Fecha o navegador após a execução
browser.quit()
