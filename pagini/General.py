"""
Marcel Matei - Web page testing project
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com')
driver.maximize_window()
driver.implicitly_wait(5)

#  buton accord gdpr prima pagina
accord_gdpr1_pagina_principala = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
accord_gdpr1_pagina_principala.click()

#   bara de cautare de pe prima pagina
bara_cautare_pagina_principala = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]')
bara_cautare_pagina_principala.is_displayed()
driver.save_screenshot('evidence_pagina_principala.png')

#   meniu principal dreapta sus - optiuni cautare
mainMenu_imagini_pagina_principala = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[2]/a')
mainMenu_imagini_pagina_principala.click()

#   accord gdpr pagina cautare imagini
accord_gdpr2_cautare_imagini = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
accord_gdpr2_cautare_imagini.click()

#   logoul google pentru pagina de cautare imagini
logo_google_imagini = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/img')
logo_google_imagini.is_displayed()

#   bara de cautare google - pagina cautare imagini
bara_cautare_google_imagini1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div['
                                                             '1]/div/div[2]/input')
bara_cautare_google_imagini1.send_keys('pisica')

#   buton/enter din bara de cautare din pagina cautare imagini
buton_cautare_google_imagini1 = driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div')
buton_cautare_google_imagini1.click()

#   optiunea de cautare stiri
meniu_stiri_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div['
                                                                     '1]/div[1]/div/div/a[3]')
meniu_stiri_pagina_rezultate_imagini.click()

#   hint-ul de rezultate estimative de pe pagina de rezultate stiri
rezultate_estimative_pagina_stiri = driver.find_element(By.ID, 'result-stats')
rezultate_estimative_pagina_stiri.is_displayed()

#   bara footer din pagina rezultate stiri
footer_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fbar"]/div[3]')
footer_pagina_rezultate_imagini.is_displayed()

#   buton/hiperlink catre pagina Ajutor de pe pagina rezultate stiri
buton_ajutor_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fsl"]/a[1]')
buton_ajutor_pagina_rezultate_imagini.is_displayed()

#   buton/hiperlink catre pagina de Feedback de pe pagina rezultate stiri
buton_trimitefdbk_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="dk2qOd"]')
buton_trimitefdbk_pagina_rezultate_imagini.is_displayed()

#   buton/hiperlink catre pagina Confidentialitate de pe pagina rezultate stiri
buton_confidentialitate_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fsl"]/a[3]')
buton_confidentialitate_pagina_rezultate_imagini.is_displayed()

#   buton/hiperlink catre pagina Termeni de pe pagina rezultate stiri
buton_termeni_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fsl"]/a[4]')
buton_termeni_pagina_rezultate_imagini.is_displayed()


buton_ajutor_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fsl"]/a[1]')
buton_ajutor_pagina_rezultate_imagini.click()

#   lista dropdown cu optiunile de limbi disponibile
lista_dropdown_limbi = driver.find_element(By.XPATH, '//*[@id="hcfe-content"]/footer/div/div[1]/form/div')
lista_dropdown_limbi.is_displayed()

#   butonul pentru lista cu optiunile de limbi disponibile
buton_dropdown_lista_limbi_ajutor = driver.find_element(By.CSS_SELECTOR, '#hcfe-content > footer > div > '
                                                                         'div:nth-child(1) > form > div > svg > path')
buton_dropdown_lista_limbi_ajutor.click()

#   buton limba engleza
buton_engleza_lista_limbi_pagina_ajutor = driver.find_element(By.ID, ':4')
buton_engleza_lista_limbi_pagina_ajutor.click()

#   titlul sectiei de subiecte dedicate
titlu_subiecte_ajutor = driver.find_element(By.XPATH, '//*[@id="hcfe-content"]/section/div/div/h2')
titlu_subiecte_ajutor.click()

driver.quit()
