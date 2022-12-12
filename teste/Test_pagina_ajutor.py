from selenium.webdriver.common.by import By

from teste.Test_pagina_cautare_imagini import TestPaginaCautareImagini
from teste.Test_pagina_principala import TestPaginaPrincipala
from teste.Test_pagina_rezultate import TestPaginaStiri


class TestPaginaAjutor(TestPaginaStiri):
    Lista_dropdown_limbi = (By.XPATH, '//*[@id="hcfe-content"]/footer/div/div[1]/form/div')
    Buton_dropdown_lista_limbi_ajutor = (By.CSS_SELECTOR, '#hcfe-content > footer > div > div:nth-child(1) > form > '
                                                          'div > svg > path')
    Buton_engleza_lista_limbi_pagina_ajutor = (By.ID, ':4')
    Titlu_subiecte_ajutor = (By.XPATH, '//*[@id="hcfe-content"]/section/div/div/h2')

    def test_optiuni_rezultate(self):
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr1_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.MainMenu_imagini_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr2_cautare_imagini).click()
        self.driver.find_element(*TestPaginaCautareImagini.Bara_cautare_google_imagini1).send_keys('pisica')
        self.driver.find_element(*TestPaginaCautareImagini.Buton_cautare_google_imagini1).click()
        self.driver.find_element(*TestPaginaStiri.Meniu_stiri_pagina_rezultate_imagini).click()
        self.driver.find_element(*TestPaginaStiri.Buton_ajutor_pagina_rezultate_stiri).click()
        self.driver.find_element(*TestPaginaAjutor.Lista_dropdown_limbi).is_displayed()
        self.driver.find_element(*TestPaginaAjutor.Buton_dropdown_lista_limbi_ajutor).click()
        self.driver.find_element(*TestPaginaAjutor.Buton_engleza_lista_limbi_pagina_ajutor).click()
        self.driver.find_element(*TestPaginaAjutor.Titlu_subiecte_ajutor).is_displayed()
        self.driver.save_screenshot('Pagina_ajutor_Engleza.png')
