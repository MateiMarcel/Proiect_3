from selenium.webdriver.common.by import By

from teste.Test_pagina_principala import TestPaginaPrincipala


class TestPaginaCautareImagini(TestPaginaPrincipala):
    #   selectori pagini cautare si rezultate imagini
    Logo_google_imagini = (By.CLASS_NAME, 'lnXdpd')
    Footer_pagina_cautare_imagini = (By.CLASS_NAME, 'KxwPGc AghGtd')
    Text_footer_despre_pag_cautare_imagini = (By.XPATH, '/html/body/div[1]/div[5]/div[2]/div[1]/a[1]')
    Text_footer_publicitate_pag_cautare_imagini = (By.XPATH, '/html/body/div[1]/div[5]/div[2]/div[1]/a[2]')
    Text_footer_companii_pag_cautare_imagini = (By.XPATH, '/html/body/div[1]/div[5]/div[2]/div[1]/a[3]')
    Text_footer_cumfunctioneaza_pag_cautare_imagini = (By.XPATH, '/html/body/div[1]/div[5]/div[2]/div[1]/a[4]')
    Bara_cautare_google_imagini1 = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    Buton_bara_cautare_cu_imagini = (By.CLASS_NAME, 'Gdd5U')
    Buton_cautare_google_imagini1 = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div')
    Rezultate_cautare_imagini = (By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]')
    Rezultat_text_pisica_pagina_rezultate = (By.CLASS_NAME, 'og3lId')

#   verificare elemente footer pagina cautare imagini
    def test_verificare_elem_pagcautareimagini(self):
        self.driver.get('https://www.google.ro/imghp?hl=en&tab=ri&ogbl')
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr2_cautare_imagini).click()
        self.driver.save_screenshot('logo_google_imagini.png')
        self.driver.find_element(*TestPaginaCautareImagini.Logo_google_imagini).is_displayed()
        self.driver.find_element(*TestPaginaCautareImagini.Buton_bara_cautare_cu_imagini)
        self.driver.find_element(*TestPaginaCautareImagini.Text_footer_despre_pag_cautare_imagini)
        self.driver.find_element(*TestPaginaCautareImagini.Text_footer_publicitate_pag_cautare_imagini)
        self.driver.find_element(*TestPaginaCautareImagini.Text_footer_companii_pag_cautare_imagini)
        self.driver.find_element(*TestPaginaCautareImagini.Text_footer_cumfunctioneaza_pag_cautare_imagini)

#   verificare functionalitate cautare pagina imagini si rezultat
    def test_cautare_pagina_imagini(self):
        self.driver.get('https://www.google.ro/imghp?hl=en&tab=ri&ogbl')
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr2_cautare_imagini).click()
        self.driver.find_element(*TestPaginaCautareImagini.Bara_cautare_google_imagini1).send_keys('pisica')
        self.driver.save_screenshot('Bara_cautare_pisica.png')
        self.driver.find_element(*TestPaginaCautareImagini.Buton_cautare_google_imagini1).click()
        self.driver.find_element(*TestPaginaCautareImagini.Rezultate_cautare_imagini).is_displayed()
        self.driver.find_element(*TestPaginaCautareImagini.Rezultat_text_pisica_pagina_rezultate).find_elements(
            By.CLASS_NAME, value='pisica')
        self.driver.save_screenshot('Pagina_rezultate_pisica.png')
