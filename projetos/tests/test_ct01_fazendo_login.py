from selenium.webdriver.common.by import By
import pytest
import conftest

@pytest.mark.usefixtures('setup_teardown')
class Test_CT01:
    def test_ct01_fazendo_login(self):
        navegador = conftest.navegador
        #user_name
        navegador.find_element(By.ID, 'user-name').send_keys('standard_user')

        #senha
        navegador.find_element(By.ID, 'password').send_keys('secret_sauce')

        #login_button
        navegador.find_element(By.ID, 'login-button').click()
        assert navegador.find_element(By.XPATH, '//*[@class="product_label"]').is_displayed()
        print('passed')
