from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

navegador = webdriver.Chrome()
wait = WebDriverWait(navegador, 20)

navegador.get(
    'https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
navegador.find_element(By.ID, 'populate-text').click()
wait.until(ec.text_to_be_present_in_element(
    (By.CLASS_NAME, 'target-text'), 'Selenium Webdriver'))
text = navegador.find_element(By.CLASS_NAME, 'target-text').text
assert text == 'Selenium Webdriver'
print('passed!!')
