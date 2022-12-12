from selenium.webdriver.common.by import By

from teste.Test_pagina_principala import TestPaginaPrincipala


class TestPaginaCautareImagini(TestPaginaPrincipala):
    Logo_google_imagini = (By.XPATH, '/html/body/div[1]/div[2]/div/img')
    Bara_cautare_google_imagini1 = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    Buton_cautare_google_imagini1 = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div')
    Rezultate_cautare_imagini = (By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]')

    def test_verificare_logo(self):
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr1_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.MainMenu_imagini_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr2_cautare_imagini).click()
        self.driver.find_element(*TestPaginaCautareImagini.Logo_google_imagini).is_displayed()
        self.driver.save_screenshot('logo_google_imagini.png')

    def test_cautare_pagina_imagini(self):
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr1_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.MainMenu_imagini_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr2_cautare_imagini).click()

        self.driver.find_element(*TestPaginaCautareImagini.Bara_cautare_google_imagini1).send_keys('pisica')
        self.driver.save_screenshot('bara_cautare_pisica.png')
        self.driver.find_element(*TestPaginaCautareImagini.Buton_cautare_google_imagini1).click()
        self.driver.save_screenshot('pagina_rezultate_pisica.png')
        self.driver.find_element(*TestPaginaCautareImagini.Rezultate_cautare_imagini).is_displayed()
