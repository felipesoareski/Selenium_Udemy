from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get('https://www.youtube.com/watch?v=lTN92QCUnC0')

#tag_name#id_value(tag é opcional)               /  navegador.find_element(By.CSS_SELECTOR, "input#password")
#tag_name.class_value(tag é opcional)           /   navegador.find_element(By.CSS_SELECTOR, "input.input_error")
#tag_name[attribute=value] (tag é opcional)    /    navegador.find_element(By.CSS_SELECTOR, "input[type=password]")
#combinar os CSS_selectors:
#tag_name.class_name[attribute=value]           /   navegador.find_element(By.CSS_SELECTOR,  "input.input_error[type=password]")

#XPATH:
#//tag ou *[@attribute= "attribute_value"]
#//tag ou *[contains(text(), "texto que esta dentro do atributo")]
#//tag ou *[contains(@attribute, "attribute_value")]
#//tag ou *[contains(@attribute, "attribute_value") and contains(text(), "texto")]