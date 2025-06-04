"""
=======================
Coletor de Dados Netshoes
=======================

Descrição:
-----------
Este script automatiza a coleta de dados de produtos no site da Netshoes utilizando Selenium. 
Ele simula a navegação de um usuário, realiza buscas por "tênis nike" e extrai os nomes 
e preços dos produtos exibidos na primeira página de resultados.

Funcionalidades:
----------------
- Acessa o site da Netshoes automaticamente.
- Preenche e envia a barra de pesquisa com um termo específico.
- Aguarda o carregamento dos resultados usando WebDriverWait.
- Extrai nome e preço de cada produto encontrado.
- Salva os dados capturados em um arquivo Excel (`relatorio.xlsx`).

Aplicação no Mundo Real:
-------------------------
Este coletor pode ser usado para:
✔ **Análise de preços** → Comparar ofertas e tendências do mercado esportivo.
✔ **Monitoramento de concorrência** → Empresas podem acompanhar preços e produtos rivais.
✔ **Automação de pesquisas** → Evita a necessidade de buscar manualmente informações repetitivas.
✔ **Ciência de dados** → Pode servir como base para modelos que analisam variação de preços ao longo do tempo.

Como Expandir:
--------------
🔹 Implementar navegação entre páginas para capturar mais resultados.
🔹 Melhorar filtros de busca para extrair produtos específicos.
🔹 Integrar com banco de dados para armazenamento e análise histórica.
🔹 Criar relatórios gráficos automáticos com os dados coletados.

Autor: Lucas  
Última Atualização: Junho/2025
"""


# Importação de bibliotecas
import csv
import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  
chrome_options.add_argument("--ignore-ssl-errors=yes")  # Ignora erros de SSL  
chrome_options.add_argument("--ignore-certificate-errors")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--disable-dev-shm-usage")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-web-security")  # Desativa algumas verificações de segurança
chrome_options.add_argument("--allow-running-insecure-content")  # Permite carregamento de páginas inseguras
chrome_options.add_argument("--disable-popup-blocking")  # Evita que pop-ups interfiram na execução
chrome_options.add_argument("--headless=new")  # Executa o Chrome sem interface gráfica (testando modo mais leve)
chrome_options.add_argument("--disable-software-rasterizer")  # Desativa renderização via software
chrome_options.add_argument("--disable-extensions")  # Evita que extensões causem erro
chrome_options.add_argument("--start-maximized")  # Evita problemas de resolução ao carregar elementos visíveis
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")




# Inicializando o WebDriver
driver = webdriver.Chrome(options=chrome_options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
precos_script = driver.execute_script("return document.querySelectorAll('.price__list--card')")

try:
    # Abrir o site da Netshoes
    driver.get("https://www.netshoes.com.br")

    # Esperar a barra de pesquisa estar visível
    wait = WebDriverWait(driver, 10)
    # Localizando a barra de pesquisa
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "search")))

    # Digitar "tênis nike" e buscar
    search_box.send_keys("tênis nike")
    search_box.send_keys(Keys.RETURN)

    # Esperar os resultados carregarem e capturar os nomes e preços dos produtos usando XPath
    wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(@class, 'product-card__title')]")))
    produtos = driver.find_elements(By.XPATH, "//h3[contains(@class, 'product-card__title')]")
    time.sleep(5)  # Espera extra para carregamento

    precos = driver.find_elements(By.XPATH, "//div[contains(@class, 'product-card')]//span[contains(@class, 'price')]")

    if not precos:
        print("❌ Nenhum preço encontrado! O XPath pode estar incorreto ou os elementos ainda não carregaram.")
    else:
        for preco in precos:
            print(f"✅ Preço encontrado: {preco.text}")



    # Criar uma nova planilha Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Netshoes Dados"

    # Adicionar cabeçalhos
    sheet.append(["Produto","Preço"])

    # Adicionar os dados à planilha
    for produto, preco in zip(produtos, precos):
        sheet.append([produto.text, preco.text])

    # Salvar o arquivo Excel
    workbook.save("data/relatorio.xlsx")

    # Mensagem de sucesso
    print("\n✅ Dados salvos em 'data/relatorio.xlsx'!")


except Exception as e:
    # Capturar erros 
    print(f"\n❌ Ocorreu um erro: {e}")


finally:
     # Fechar o navegador
     driver.quit()