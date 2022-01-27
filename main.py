## Area dos comentarios
'''
1) Pegar o conteúdo do site a partir da URL
2) Parsear o conteúdo HTML - BeaultifulSoup
3) Estruturar conteúdo em um Data Frame - Pandas
4) Transformar os Dados em um Dicionário de dados próprio
5) Enviar os dados por e-mail/zap sempre que eu ligar o pc

Video do youtube que usei como base para o Projeto
Python na Prática fazendo Web Scraping (de JavaScript dinâmico) // Mão no Código #28

Sites que me ajudaram a lidar com o chromedrive
https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
https://chromedriver.chromium.org/home
https://chromedriver.chromium.org/getting-started

Sites que me ajudaram a lidar com o Selenium
https://selenium-python.readthedocs.io/locating-elements.html

Tipos de busca .find_element
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

'''

## Bibliotecas ultilizadas
''' Instalar tudo dentro da pasta do projeto
pip install request2
pip install pandas
pip install lxml
pip install beautifulsoup4
pip install selenium
'''

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

url_celular = 'https://www.tudocelular.com/compare/6707.html'

#Configurando o projeto para rodar em segundo plano
options = Options()
options.add_argument("start-maximized")
options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get(url_celular)
time.sleep(2)

# Teste caso precise clicar em algum lugar
'''
driver.find_element(By.XPATH, "//div[@class='phone_column']//a[@class='bubble_costo green']").click()
time.sleep(10)
'''

element = driver.find_element(By.XPATH,"//div[@class='phone_column']//a[@class='bubble_costo green']")
html_content = element.get_attribute('outerHTML')

#print(html_content)

for linha in html_content.split('\n'):
    if "<strong>" in linha:
        posi = linha.find('.')
        preco = linha[posi-1:posi+4]
    if ".html" in linha:
        posi = linha.find(".html")
        modelo = linha[posi-18:posi]


mensagem = "Celular: " + modelo + " Valor atual: " + preco

print(mensagem)
driver.quit()

