from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

workspace = 1169

# Setup básico
driver = webdriver.Chrome()
driver.get("https://validacao.mitralab.io/w/1169")
time.sleep(5)

wait = WebDriverWait(driver, 10)



def criarproj():
    url = "https://api.mitrasheet.com:4129/mitraspace/project"

    headers = {
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Origin": "https://validacao.mitralab.io",
        "Referer": "https://validacao.mitralab.io/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        "accept": "application/json",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJNaXRyYSIsImp0aSI6IjEzNjg1Iiwic3ViIjoibHVpei5udW5lc0BtaXRyYWxhYi5pbyIsImlhdCI6MTc0NDY1NzgwMywidG5pIjoxNjk4NCwiYWNjZXNzVHlwZSI6IkNSRUFUT1IiLCJleHAiOjI2MDg2NTc4MDN9.dnYF0gAQpFsrJjqudLGOxOSGivdlmkd_wIOPJqEtD0Y",
        "cache-control": "no-cache",
        "content-type": "application/json",
    }
    data = {
        "iconFile": None,
        "locale": "pt_BR",
        "workspaceId": 10483,
        "name": "Teste QA Automação",
        "baseMergeBackupUrl": "backup/store/pesquisaSatisfação/pesquisaSatisfação.zip",
        "bucketSource": "mitra-multitenant-prod",
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

# Dados
email = "luiz.nunes@mitralab.io"
passw = "Lipe123"

# Email
input_email = wait.until(EC.presence_of_element_located((By.ID, "login_form_email")))
input_email.send_keys(email)

# Preenche a senha
input_senha = driver.find_element(By.ID, "login_form_password")
input_senha.send_keys(passw)

# Clica no botão de login (usando XPath mais robusto)
botao_login = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[contains(@class, 'login-button')]//span[contains(text(), 'Login')]")
))
botao_login.click()

time.sleep(100)
