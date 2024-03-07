
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

navegador = webdriver.Chrome()
navegador.get('https://chercher.tech/practice/frames')
wait = WebDriverWait(navegador, 10)
wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@style="font-size:40px;"]')))

maxframe = navegador.find_element(By.ID, 'frame1')
navegador.switch_to.frame(maxframe)
frame1 = navegador.find_element(By.XPATH, '//*[@id="topic"]/following-sibling::input')
assert frame1.is_displayed()
frame1.send_keys('frame1')
print('frame1: passed')

sleep(2)

frame3 = navegador.find_element(By.ID, 'frame3')
navegador.switch_to.frame(frame3)
frame3 = navegador.find_element(By.XPATH, '//*[@type="checkbox"]')
frame3.click()
assert frame3.is_selected()
print('frame3: passed')
sleep(2)
navegador.switch_to.default_content()

frame2 = navegador.find_element(By.ID, 'frame2')
navegador.switch_to.frame(frame2)
dropdown_animals = Select(navegador.find_element(By.XPATH, '//*[@id="animals"]'))
dropdown_animals.select_by_visible_text("Big Baby Cat")
assert dropdown_animals.first_selected_option.text == 'Big Baby Cat'
print('first_selected: passed')

