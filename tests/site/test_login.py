from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class TestLogin:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
    

    def test_login(self):
        # define qual pagina o browser deve abrir 
        driver.get('https://github.com')

        btn_link_sign_in = driver.find_element(By.CLASS_NAME, 'HeaderMenu-link--sign-in')
        btn_link_sign_in.click()

        # Realiza um print da tela
        driver.save_screenshot('screen_00.png')

        # Depois de 2 segundos a página fecha
        time.sleep(2)


        field_login = driver.find_element(By.ID, 'login_field')
        field_login.send_keys('email@gmail.com')


        field_password = driver.find_element(By.ID, 'password')
        field_password.send_keys('ezequais')


         # Realiza um print da tela
        driver.save_screenshot('screen_01.png')

        field_password.send_keys(Keys.RETURN)

         # Depois de 2 segundos a página fecha
        time.sleep(2)


        label_result = driver.find_element(By.CLASS_NAME, 'js-flash-alert')


         # Realiza um print da tela
        driver.save_screenshot('screen_02.png')
 

        print(label_result.text)

        assert 'Incorrect username or password' in label_result.text


    def teardown_class(self):
        driver.close()