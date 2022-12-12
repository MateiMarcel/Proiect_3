import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPaginaPrincipala(unittest.TestCase):
    Accord_gdpr1_pagina_principala = (By.XPATH, '//*[@id="L2AGLb"]/div')
    Bara_cautare_pagina_principala = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]')
    MainMenu_imagini_pagina_principala = (By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[2]/a')
    Accord_gdpr2_cautare_imagini = (By.XPATH, '//*[@id="L2AGLb"]/div')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.google.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_accord_gdpr1(self):
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr1_pagina_principala).click()
        self.driver.save_screenshot('accord_gdpr1.png')

    def test_bara_cautare_pagina_principala(self):
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr1_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.Bara_cautare_pagina_principala).is_displayed()
        self.driver.save_screenshot('bara_cautare_pagina_pricipala.png')

    def test_mainmenu_buton_imagini(self):
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr1_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.MainMenu_imagini_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr2_cautare_imagini).click()
        self.driver.save_screenshot('pagina_cautare_imagini.png')
