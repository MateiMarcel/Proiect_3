from selenium.webdriver.common.by import By

from teste.Test_pagina_rezultate_stiri import TestPaginaStiri


class TestPaginaAjutor(TestPaginaStiri):
    #   selectori pagina ajutor
    Lista_dropdown_limbi = (By.XPATH, '//*[@id="hcfe-content"]/footer/div/div[1]/form/div')
    Buton_dropdown_lista_limbi_ajutor = (By.CSS_SELECTOR, '#hcfe-content > footer > div > div:nth-child(1) > form > '
                                                          'div > svg > path')
    Buton_romana_lista_limbi_pagina_ajutor = (By.ID, ':17')
    Buton_engleza_lista_limbi_pagina_ajutor = (By.ID, ':4')
    Titlu_subiecte_ajutor = (By.XPATH, '//*[@id="hcfe-content"]/section/div/div/h2')
    Logo_google_pagina_ajutor = (By.XPATH, '/html/body/div[2]/header/div[4]/a/div/img')

    #   test pagina ajutor - verificare elemente si functionalitate
    def test_pagina_ajutor(self):
        self.driver.get(
            'https://support.google.com/websearch/?visit_id=638067109786373832-2023441399&hl=en-RO&rd=2#topic=3378866')
        self.driver.find_element(*TestPaginaAjutor.Lista_dropdown_limbi).is_displayed()
        self.driver.find_element(*TestPaginaAjutor.Buton_dropdown_lista_limbi_ajutor).click()
        self.driver.find_element(*TestPaginaAjutor.Buton_romana_lista_limbi_pagina_ajutor).click()
        self.driver.save_screenshot('Pagina_ajutor_Romana.png')
        self.driver.find_element(*TestPaginaAjutor.Buton_dropdown_lista_limbi_ajutor).click()
        self.driver.find_element(*TestPaginaAjutor.Buton_engleza_lista_limbi_pagina_ajutor).click()
        self.driver.save_screenshot('Pagina_ajutor_select_engleza.png')
        self.driver.find_element(*TestPaginaAjutor.Titlu_subiecte_ajutor).is_displayed()
        self.driver.find_element(*TestPaginaAjutor.Logo_google_pagina_ajutor).is_displayed()
        self.driver.save_screenshot('Pagina_ajutor_Engleza.png')
