from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

def launchBrowser():
    # essa função será responsável por realizar a busca na amazon e encontrar os 3 resultados, com seus nomes e preços
    
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

    URL = 'https://www.amazon.com.br'

    produto = "samsung galaxy smartphone"

    driver.get(URL)

    # encontra a text area para realizar a pesquisa, pesquisa o produto e dá enter
    text_area = driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

    text_area.send_keys(produto)
    text_area.send_keys(Keys.ENTER)

    # pega os resultados através do seletor
    elementos = driver.find_elements(By.CSS_SELECTOR, '[role="listitem"]')

    # similar ao desafio 3, os resultados serão armazenados em um array de dicionários
    resultados = []

    try: 
        # itera os elementos encontrados até o número limite, pegando seu nome e preço completo
        for i, element in enumerate(elementos, start=1):
            if i >= 4:
                break

            # encontra o nome do produto
            h2_nome_produto = element.find_element(By.CSS_SELECTOR, 'h2.a-size-base-plus.a-spacing-none.a-color-base.a-text-normal')
            nome_produto = h2_nome_produto.find_element(By.CSS_SELECTOR, 'span').text

            # encontra o preço do produto
            simbolo_preco = element.find_element(By.CSS_SELECTOR, 'span.a-price-symbol').text
            numero_preco = element.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
            decimal_preco = element.find_element(By.CSS_SELECTOR, 'span.a-price-fraction').text

            preco = f"{simbolo_preco}{numero_preco}.{decimal_preco}"

            resultados.append({
                'nome_produto': nome_produto,
                'preco': preco
            })
    except Exception as e:
        print(f"Ocorreu uma exceção: {e}")
    
    driver.quit()
    return resultados

def main():
    # a main irá chamar a função do selenium e realizar o print do resultado

    resultados = launchBrowser()

    # itera o array para printar os resultados finais
    for i, item in enumerate(resultados, start=1):

        print(f"{i}. {item['nome_produto']} - {item['preco']}")

if __name__ == "__main__":
    main()
