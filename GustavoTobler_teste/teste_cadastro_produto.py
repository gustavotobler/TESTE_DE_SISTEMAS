from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Configuração do WebDriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

#Acessa a página de cadastro usando o caminho absoluto com o protocolo file://
#Certifique-se de que o caminho está apontando para um arquivo HTML específico

driver.get("C:/Users/gustavo_tobler/Documents/GitHub/TESTE_DE_SISTEMAS/produtos.html")

#Preenche o campo produto
produto_input = driver.find_element(By.ID, "produto")
produto_input.send_keys("Mortadela")

#Preenche o campo descrição
descricao_input = driver.find_element(By.ID, "descricao")
descricao_input.send_keys("Mortadela")

#Preenche o campo marca
marca_input = driver.find_element(By.ID, "marca")
marca_input.send_keys("Sádia")

#Preenche o campo quantidade
quant_input = driver.find_element(By.ID, "quant")
quant_input.send_keys("100")

#Preenche o campo preço
preco_input = driver.find_element(By.ID, "preco")
preco_input.send_keys("10")

#Clica no botão de Cadastrar
#submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#submit_button.click()

#Aguarda um momento para visualizar o resultado (em uma aplicação real, você verificaria a resposta)
#time.sleep(2000)

#Fecha o navegador
#driver.quit()