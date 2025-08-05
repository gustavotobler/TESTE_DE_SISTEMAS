from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/TESTE_DE_SISTEMAS/login.html")

time.sleep(1)

#Preenche os campos

driver.find_element(By.ID, "username"). send_keys("admin")
driver.find_element(By.ID, "password"). send_keys("123456d")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(8)
if "Cadastro de Cliente" in driver.page_source:
    print("Login realizado com sucesso!")
else:
    print("Falha no login.")