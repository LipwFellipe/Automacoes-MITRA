from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import time

email = "luiz.nunes@mitralab.io"
passw = "Lipe123"
perg = ("1- Crie um CRUD de vendedores, coloque atributos que são comuns para cadastros de vendedores",
        "2- Crie uma nova tela com inputs pra cada um dos campos da tabela vendedor para substituirem o formulário de edição, vamos dps clicar na list que fica nessa tela e abrir o modal com esses inputs para que a gente possa alterar os atributos dos vendedores",
        "3- Agora crie uma FK chamada “gerente” apontando pra uma nova tabela, crie uns membros pra gerente e adicione um input na tela editar vendedor pra gente poder alterar o gerente do vendedor com um droplist",
        "4- crie uma tabela de vendas, lance umas vendas exemplo e faça um dashboard com vendas por vendedor, vendas por dia e 3 cards: 1 com o total de vendas, 1 com volume de vendas e 1 com ticket médio. Coloque filtros de data, vendedor, produto e gerente",
        "5- adicione um quadrante aqui com a venda por gerente, coloque títulos pros gráficos")
i = 0
workspace = 1169

def criarproj():
    print("Criando projeto...")
    url = "https://api0.mitraecp.com:1005/mitraspace/project"

    headers = {
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Origin": "https://validacao.mitralab.io",
        "Referer": "https://validacao.mitralab.io/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        "accept": "application/json",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJNaXRyYSIsImp0aSI6IjI3MTYiLCJzdWIiOiJsdWl6LmZlbGxpcGUubnVuZXMyMDE2QGdtYWlsLmNvbSIsImlhdCI6MTc0NDgyNTkzNiwidG5pIjoxMDU5NCwiYWNjZXNzVHlwZSI6IkNSRUFUT1IiLCJleHAiOjI2MDg4MjU5MzZ9.SjuUMZ6csAdkIv6N_EFkJFIPZhLZw5JmLc49qX-CkRQ",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "sec-ch-ua": "Microsoft Edge;v=135, Not-A.Brand;v=8, Chromium;v=135",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows"
    }
    data = {
        "iconFile": None,
        "locale": "pt_BR",
        "workspaceId": 1169,
        "name": "16-04 Automatizado2",
        "projectConfig": {
            "color": "#7839EE",
            "icon": "initials"
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("✅ Projeto criado com sucesso!")
        print(response.json())
        return response.json().get("id")
projeto = criarproj()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(f"https://validacao.mitralab.io/w/{workspace}/p/{projeto}")
time.sleep(5)

# Fazer Login

input_email = wait.until(EC.presence_of_element_located((By.ID, "login_form_email")))
input_email.send_keys(email)

input_senha = driver.find_element(By.ID, "login_form_password")
input_senha.send_keys(passw)

botao_login = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[contains(@class, 'login-button')]//span[contains(text(), 'Login')]")))
botao_login.click()

time.sleep(3)

driver.get(f"https://validacao.mitralab.io/w/{workspace}/p/{projeto}")

inputIA = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//textarea[@placeholder="Send a new message..."]')))
inputIA.send_keys(perg[i])
inputIA.send_keys(Keys.ENTER)
i += 1


# Ver o texto grande
"""
- Mandar pergunta 1
- Espera até aparecer a tool ou o JSON
---if Json : manda rodar a tool
----- if 
- else 
- Espera para apertar em executar a tool
""""


time.sleep(1000)


