from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

def launchBrowser():
    # essa função será responsável por abrir o google, realizar a pesquisa e obter os 5 primeiros resultados da busca

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

    URL = 'https://www.google.com'

    driver.get(URL)
    
    string_busca = "Python Selenium"

    try:
        # encontra a caixa de texto, escreve a string de busca e dá enter
        text_area = driver.find_element(By.CSS_SELECTOR, 'textarea#APjFqb.gLFyf')

        text_area.send_keys(string_busca)
        text_area.send_keys(Keys.ENTER)
        
        # os resultados serão armazenados em uma lista, em forma de dicionários
        resultados = []

        # os outputs da busca do google foram filtrados pela sua classe, excluindo a classe pai para o caso de vídeos e a classe filho para o caso de dropdowns
        google_output = driver.find_elements(By.XPATH,
                                                '//div[contains(@class, "MjjYud")][not(ancestor::*[contains(@class, "ULSxyf")])][not(descendant::*[contains(@class, "cUnQKe")])]'
                                            )

        for i, element in enumerate(google_output, start=0):
            # número limite
            if i >=5:
                break

            try:
                # encontra o titulo e o link de cada resultado da pesquisa e os armazena no array em formato de dicionario
                titulo = element.find_element(By.XPATH, './/h3[contains(@class, "LC20lb")]').text
                link = element.find_element(By.XPATH, './/a[contains(@class, "zReHs")]').get_attribute('href')
                
                resultados.append({
                    'titulo': titulo,
                    'link': link
                })

            except Exception as e:
                print(f"Erro encontrado: {e}")

    except (NoSuchElementException) as e:
        print("Elemento não encontrado")

    driver.quit()
    return resultados

def main():
    # a main irá chamar a função do selenium e realizar o print do resultado

    resultados = launchBrowser()

    # itera o array para printar os resultados finais
    for i, item in enumerate(resultados, start=1):

        print(f"{i}. {item['titulo']} - {item['link']}")

if __name__ == "__main__":
    main()

