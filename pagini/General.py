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

#   click pe buton accord gdpr prima pagina
accord_gdpr1_pagina_principala = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
accord_gdpr1_pagina_principala.click()

#   verificare bara de cautare de pe prima pagina
bara_cautare_pagina_principala = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]')
bara_cautare_pagina_principala.is_displayed()
driver.save_screenshot('evidence_pagina_principala.png')

#   verificare prezenta buton Gmail din meniu principal
buton_gmail_meniu_principal = driver.find_element(By.CLASS_NAME, 'gb_j')
buton_gmail_meniu_principal.is_displayed()

#   verificare prezenta buton optiuni din meniu principal (patrat)
buton_dropdown_restul_optiunilor = driver.find_element(By.XPATH, '//*[@id="gbwa"]/div/a/svg')
buton_dropdown_restul_optiunilor.is_displayed()

#   click pe meniu principal dreapta sus - optiuni cautare imagini
mainMenu_imagini_pagina_principala = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[2]/a')
mainMenu_imagini_pagina_principala.click()

#   accord gdpr pagina cautare imagini
accord_gdpr2_cautare_imagini = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
accord_gdpr2_cautare_imagini.click()

#   verificare prezenta logo google imagini
logo_google_imagini = driver.find_element(By.CLASS_NAME, 'lnXdpd')
logo_google_imagini.is_displayed()

#   verificare prezenta buton cautere cu imagini
buton_bara_cautare_cu_imagini = driver.find_element(By.CLASS_NAME, 'Gdd5U')
buton_dropdown_restul_optiunilor.is_displayed()

#   verificare prezenta footer pagina cautare imagini
footer_pagina_cautare_imagini = driver.find_element(By.CLASS_NAME, 'KxwPGc AghGtd')
footer_pagina_cautare_imagini.is_displayed()

#   verificare prezenta 'despre' footer pagina cautare imagini
text_footer_despre_pag_cautare_imagini = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/div[1]/a[1]')
text_footer_despre_pag_cautare_imagini.is_displayed()

#   verificare prezenta 'publicitate' footer pagina cautare imagini
text_footer_publicitate_pag_cautare_imagini = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/div['
                                                                            '1]/a[2]')
text_footer_publicitate_pag_cautare_imagini.is_displayed()

#   verificare prezenta 'companiifooter pagina cautare imagini
text_footer_companii_pag_cautare_imagini = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/div[1]/a[3]')
text_footer_companii_pag_cautare_imagini.is_displayed()

#   verificare prezenta 'cumfunctioneaza' footer pagina cautare imagini
text_footer_cumfunctioneaza_pag_cautare_imagini = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/div['
                                                                                '1]/a[4]')
text_footer_cumfunctioneaza_pag_cautare_imagini.is_displayed()

#   introducere value pentru cautare imagini - bara de cautare google - pagina cautare imagini
bara_cautare_google_imagini1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div['
                                                             '1]/div/div[2]/input')
bara_cautare_google_imagini1.send_keys('pisica')

#   click pe buton cautare din bara cautare imagini
buton_cautare_google_imagini1 = driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div')
buton_cautare_google_imagini1.click()

#   click pe optiunea de cautare stiri
meniu_stiri_pagina_rezultate_imagini = driver.find_element(By.CLASS_NAME, 'NZmxZe')
meniu_stiri_pagina_rezultate_imagini.click()

#   verificare hint-ul de rezultate estimative de pe pagina de rezultate stiri
rezultate_estimative_pagina_stiri = driver.find_element(By.ID, 'result-stats')
rezultate_estimative_pagina_stiri.is_displayed()

#   verificare bara footer din pagina rezultate stiri
footer_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fbar"]/div[3]')
footer_pagina_rezultate_imagini.is_displayed()

#   verificare prezenta buton/hiperlink catre pagina Ajutor de pe pagina rezultate stiri
buton_ajutor_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fsl"]/a[1]')
buton_ajutor_pagina_rezultate_imagini.is_displayed()

#   verificare prezenta buton/hiperlink catre pagina de Feedback de pe pagina rezultate stiri
buton_trimitefdbk_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="dk2qOd"]')
buton_trimitefdbk_pagina_rezultate_imagini.is_displayed()

#   verificare prezenta buton/hiperlink catre pagina Confidentialitate de pe pagina rezultate stiri
buton_confidentialitate_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fsl"]/a[3]')
buton_confidentialitate_pagina_rezultate_imagini.is_displayed()

#   verificare prezenta buton/hiperlink catre pagina Termeni de pe pagina rezultate stiri
buton_termeni_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fsl"]/a[4]')
buton_termeni_pagina_rezultate_imagini.is_displayed()

#   click pe buton Ajutor din footer pagina rezultate stiri
buton_ajutor_pagina_rezultate_imagini = driver.find_element(By.XPATH, '//*[@id="fsl"]/a[1]')
buton_ajutor_pagina_rezultate_imagini.click()

#   verificare prezenta lista dropdown cu optiunile de limbi disponibile
lista_dropdown_limbi = driver.find_element(By.XPATH, '//*[@id="hcfe-content"]/footer/div/div[1]/form/div')
lista_dropdown_limbi.is_displayed()

#   click pe butonul pentru lista cu optiunile de limbi disponibile
buton_dropdown_lista_limbi_ajutor = driver.find_element(By.CSS_SELECTOR, '#hcfe-content > footer > div > '
                                                                         'div:nth-child(1) > form > div > svg > path')
buton_dropdown_lista_limbi_ajutor.click()

#   click pe limba engleza
buton_engleza_lista_limbi_pagina_ajutor = driver.find_element(By.ID, ':4')
buton_engleza_lista_limbi_pagina_ajutor.click()

#   verificare prezenta titlul sectiei de subiecte dedicate in limba selectata
titlu_subiecte_ajutor = driver.find_element(By.XPATH, '//*[@id="hcfe-content"]/section/div/div/h2')
titlu_subiecte_ajutor.click()

#   verificare logo google din pagina ajutor
logo_google_pagina_ajutor = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[4]/a/div/img')
logo_google_pagina_ajutor.is_displayed()

driver.quit()
