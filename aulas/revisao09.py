from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

URL = 'https://chercher.tech/practice/practice-dropdowns-selenium-webdriver'
FIRST_DROPDOWN_XPATH = '//select[@id="first"]'

navegador = webdriver.Chrome()
navegador.get(URL)

wait = WebDriverWait(navegador, 10)

# Aguardar até que o dropdown esteja presente e visível
dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, FIRST_DROPDOWN_XPATH)))
dropdown = Select(dropdown)

# Selecionar uma opção e fazer asserções
dropdown.select_by_visible_text('Yahoo')
assert dropdown.first_selected_option.text == 'Yahoo'
assert any(option.text == 'Yahoo' for option in dropdown.options)
assert not dropdown.is_multiple
print('passed')

# Verificar se o dropdown ainda está visível
mesmo_dropdown = navegador.find_element(By.XPATH, FIRST_DROPDOWN_XPATH)
assert mesmo_dropdown.is_displayed()
print('passed')

# Fechar o navegador
navegador.quit()
