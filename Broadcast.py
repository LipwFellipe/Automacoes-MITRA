from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Dados
workspace = 10483
email = "luiz.nunes@mitralab.io"
passw = "Lipe123"

def criarproj():
    url = "https://api.mitrasheet.com:4129/mitraspace/project"

    headers = {
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Origin": "https://app.mitralab.io",
        "Referer": "https://app.mitralab.io/",
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

def editarbanco():
    url = "https://api.mitrasheet.com:4088/mergeDimensionContent/"

    headers = {
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Origin": "https://app.mitralab.io",
        "Referer": "https://app.mitralab.io/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        "accept": "application/json",
        "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJsdWl6Lm51bmVzQG1pdHJhbGFiLmlvIiwiWC1UZW5hbnRJRCI6InRlbmFudF8xNzAxMiJ9.dCfvHwE_O5X9G1YMPr_I2V8MbqDBPaxPqg-kEQ7w_IRplsqcTo4449oKzc8Goo_8-wf7SAXg-Jt3bMQIG9CG6Q",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "sec-ch-ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }
    data = {
        "id": {
            "id": 1006,
            "mergeDimensionAttributeType": "DIMENSION_MAIN"
        },
        "dimensionId": 1006,
        "dimensionContentForms": [
            {
                "internalId": "1",
                "dimensionContentAttributeForms": [
                    {
                        "id": {
                            "id": 56,
                            "mergeDimensionAttributeType": "CUBE",
                            "lowCodeName": None,
                            "dataType": "VARCHAR",
                            "canUpdate": True
                        },
                        "value": f"{email}"
                    }
                ]
            }
        ]
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Dados alterados com sucesso!")

driver = webdriver.Chrome()

# Cria o projeto
projeto = criarproj()

# Aguarda até ter um ID válido
while not projeto:
    print("⏳ Aguardando criação do projeto...")
    time.sleep(1)
    projeto = criarproj()

# Depois de criado com sucesso, acessa o link
driver.get(f"https://app.mitralab.io/w/{workspace}/p/{projeto}/m/1?screenId=10")

# Agora edita o banco
editarbanco()

# Espera os elementos e faz o login
wait = WebDriverWait(driver, 10)

input_email = wait.until(EC.presence_of_element_located((By.ID, "login_form_email")))
input_email.send_keys(email)

input_senha = driver.find_element(By.ID, "login_form_password")
input_senha.send_keys(passw)

botao_login = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[contains(@class, 'login-button')]//span[contains(text(), 'Login')]")
))
botao_login.click()
time.sleep(2)
driver.get(f"https://app.mitralab.io/w/{workspace}/p/{projeto}/m/1?screenId=10")
time.sleep(1000)
driver.quit()
