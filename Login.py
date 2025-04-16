from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup básico
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://app.mitralab.io/login")
time.sleep(5)
time.sleep(1000000)

wait = WebDriverWait(driver, 10)

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
