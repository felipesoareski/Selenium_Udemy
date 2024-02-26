from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

navegador = webdriver.Chrome()
wait = WebDriverWait(navegador, 20)

navegador.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
navegador.find_element(By.XPATH, '//*[@class = "btn btn-primary btn-xs"]').click()
checkbox = navegador.find_element(By.ID, 'ch')
wait.until(ec.element_to_be_selected(checkbox))
