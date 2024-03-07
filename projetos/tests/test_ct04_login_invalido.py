from selenium import webdriver
from selenium.webdriver.common.by import By
import conftest
import pytest

@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login_invalido
class Test_CT04:
    def test_ct04_login_invalido(self):
        navegador = conftest.navegador

        navegador = webdriver.Chrome()

        navegador.get('https://www.saucedemo.com/v1/index.html')

        navegador.find_element(By.ID, 'user-name').send_keys('standard_user')
        navegador.find_element(By.ID, 'password').send_keys('451212sdsda52125we')
        navegador.find_element(By.ID, 'login-button').click()
        assert navegador.find_element(By.XPATH, '//*[@class="error-button"]').is_displayed()

