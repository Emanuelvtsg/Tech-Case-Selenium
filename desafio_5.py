from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

def launchBrowser():
    # essa função irá fazer o login no site e checar se o login foi concluído com sucesso
    
    # adicionando opções para parecer um usuário real e entrar logado, evitando aparecer captcha
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    options.add_argument(r"user-data-dir=C:\Users\Emanuel\AppData\Local\Google\Chrome\User Data")
    options.add_argument("profile-directory=Default")

    driver = webdriver.Chrome(options=options)
    
    # adiciona um wait implícito de 10s para todas ações
    driver.implicitly_wait(10)

    URL = 'https://www.saucedemo.com'

    login = "standard_user"
    senha = "secret_sauce"

    driver.get(URL)

    # pega as áreas de texto do username e da senha
    text_area_username = driver.find_element(By.CSS_SELECTOR, 'input#user-name')
    
    text_area_senha = driver.find_element(By.CSS_SELECTOR, 'input#password')

    # escreve o login e a senha
    text_area_username.send_keys(login)
    text_area_senha.send_keys(senha)

    # dá enter no botão de login
    login_botao = driver.find_element(By.CSS_SELECTOR, 'input#login-button')
    login_botao.send_keys(Keys.ENTER)
    
    # verifica se o login foi realizado e retorna uma mensagem de acordo
    mensagem_final = ""
    try:
        driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
        mensagem_final = "O login foi realizado com sucesso!"
    except NoSuchElementException:
        mensagem_final = "O elemento não foi encontrado, provavelmente você não conseguiu realizar o login! :("
    
    driver.quit()
    return mensagem_final

def main():
    # a main irá chamar a função do selenium e printar a mensagem final

    mensagem_final = launchBrowser()

    print(mensagem_final)

if __name__ == "__main__":
    main()