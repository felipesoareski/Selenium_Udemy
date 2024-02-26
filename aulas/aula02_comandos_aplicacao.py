from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get('https://www.saucedemo.com/v1/inventory.html')

#title
print(f'O titulo da pagina é: {navegador.title}')

#current_url
print(f'A url da pagina é: {navegador.current_url}')

# page_source
print(f'O codigo fonte da pagina é: {navegador.page_source}')
