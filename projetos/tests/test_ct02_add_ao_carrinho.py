from selenium.webdriver.common.by import By
import conftest
import pytest

@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.carrinho
class Test_CT02:
    def test_ct02_add_to_carrinho(self):
        navegador = conftest.navegador
        # user_name
        navegador.find_element(By.ID, 'user-name').send_keys('standard_user')

        # senha
        navegador.find_element(By.ID, 'password').send_keys('secret_sauce')

        # login_button
        navegador.find_element(By.ID, 'login-button').click()

        # adding to carrinho
        navegador.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').click()

        # clicar no botao add_carrinho e confere se o botao muda para remove
        add_to_cart = navegador.find_element(By.XPATH, '//*[@class="btn_primary btn_inventory"]')
        assert add_to_cart.is_displayed()
        add_to_cart.click()

        remove_button = navegador.find_element(By.XPATH, '//*[@class="btn_secondary btn_inventory"]')
        assert remove_button.is_displayed()

        # entra no carrinho e confere se o item foi adicionado
        carrinho = navegador.find_element(By.XPATH, '//*[@class="svg-inline--fa fa-shopping-cart fa-w-18 fa-3x "]')
        carrinho.click()
        assert navegador.find_element(
            By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed()

        # add mais um produto ao carrinho
        navegador.find_element(By.XPATH, '//a[@class="btn_secondary"]').click()
        navegador.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Fleece Jacket"]').click()

        # verificando se a imaigem e o botao add_to_cart foram mostrados
        assert navegador.find_element(By.XPATH, '//*[@class="inventory_details_img"]').is_displayed()
        assert navegador.find_element(By.XPATH, '//*[@class="btn_primary btn_inventory"]').is_displayed()

        # clica no botao add_to_cart e verifica se o botao mudou para remove
        navegador.find_element(By.XPATH, '//*[@class="btn_primary btn_inventory"]').click()
        assert navegador.find_element(By.XPATH, '//*[@class="btn_secondary btn_inventory"]').is_displayed()
        print('passed')

        carrinho = navegador.find_element(By.XPATH, '//*[@class="svg-inline--fa fa-shopping-cart fa-w-18 fa-3x "]')
        carrinho.click()
        assert navegador.find_element(
            By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed()
        assert navegador.find_element(
            By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Fleece Jacket"]').is_displayed()
        print('passed')
