from selenium.webdriver.common.by import By

from teste.Test_pagina_cautare_imagini import TestPaginaCautareImagini
from teste.Test_pagina_principala import TestPaginaPrincipala


class TestPaginaStiri(TestPaginaCautareImagini):
    Meniu_optiuni_rezultate = (By.CSS_SELECTOR, '#yDmH0d > div.T1diZc.KWE8qe > c-wiz > div.ndYZfc > div > div.tAcEof '
                                                '> div.O850f > div > div')
    Meniu_stiri_pagina_rezultate_imagini = (By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div['
                                                      '1]/div/div/a[3]')
    Rezultate_estimative_pagina_stiri = (By.ID, 'result-stats')
    Footer_pagina_rezultate_stiri = (By.XPATH, '//*[@id="fbar"]/div[3]')
    Buton_ajutor_pagina_rezultate_stiri = (By.XPATH, '//*[@id="fsl"]/a[1]')
    Buton_trimitefdbk_pagina_rezultate_stiri = (By.XPATH, '//*[@id="dk2qOd"]')
    Buton_confidentialitate_pagina_rezultate_stiri = (By.XPATH, '//*[@id="fsl"]/a[3]')
    Buton_termeni_pagina_rezultate_stiri = (By.XPATH, '//*[@id="fsl"]/a[4]')

    def test_optiuni_rezultate(self):
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr1_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.MainMenu_imagini_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr2_cautare_imagini).click()
        self.driver.find_element(*TestPaginaCautareImagini.Bara_cautare_google_imagini1).send_keys('pisica')
        self.driver.find_element(*TestPaginaCautareImagini.Buton_cautare_google_imagini1).click()
        self.driver.find_element(*TestPaginaStiri.Meniu_optiuni_rezultate).is_displayed()
        self.driver.find_element(*TestPaginaStiri.Meniu_stiri_pagina_rezultate_imagini).click()
        self.driver.find_element(*TestPaginaStiri.Rezultate_estimative_pagina_stiri).is_displayed()
        self.driver.save_screenshot('Pagina_rezultate_stiri.png')

    def test_pagina_stiri(self):
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr1_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.MainMenu_imagini_pagina_principala).click()
        self.driver.find_element(*TestPaginaPrincipala.Accord_gdpr2_cautare_imagini).click()
        self.driver.find_element(*TestPaginaCautareImagini.Bara_cautare_google_imagini1).send_keys('pisica')
        self.driver.find_element(*TestPaginaCautareImagini.Buton_cautare_google_imagini1).click()
        self.driver.find_element(*TestPaginaStiri.Meniu_stiri_pagina_rezultate_imagini).click()
        self.driver.find_element(*TestPaginaStiri.Footer_pagina_rezultate_stiri).is_displayed()
        self.driver.find_element(*TestPaginaStiri.Buton_ajutor_pagina_rezultate_stiri).is_displayed()
        self.driver.find_element(*TestPaginaStiri.Buton_trimitefdbk_pagina_rezultate_stiri).is_displayed()
        self.driver.find_element(*TestPaginaStiri.Buton_confidentialitate_pagina_rezultate_stiri).is_displayed()
        self.driver.find_element(*TestPaginaStiri.Buton_termeni_pagina_rezultate_stiri).is_displayed()
        self.driver.find_element(*TestPaginaStiri.Buton_ajutor_pagina_rezultate_stiri).click()
        self.driver.save_screenshot('Pagina_ajutor.png')
