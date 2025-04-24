from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
from fpdf import FPDF

def launchBrowser():
    # função que irá automatizar a tarefa de acessar o site, preencher a caixa de texto e realizar o download do .txt, retornando o caminho dele

    # adicionando opções para parecer um usuário real e entrar logado, evitando aparecer captcha
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    options.add_argument(r"user-data-dir=C:\Users\Emanuel\AppData\Local\Google\Chrome\User Data")
    options.add_argument("profile-directory=Default")

    output_dir = os.path.join(os.getcwd(), 'output')
    # options para o download, como não abrir popup de download e diretorio default
    options.add_experimental_option('prefs', {
        'download.default_directory': output_dir,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })

    driver = webdriver.Chrome(options=options)
    
    # adiciona um wait implícito de 10s para todas ações
    driver.implicitly_wait(10)

    URL = 'https://demo.automationtesting.in/FileDownload.html'

    driver.get(URL)
    
    texto = "Este é o último desafio do teste técnico da Port Promotora. Nele aprendi formas de utilizar Selenium"
    
    # pega a text_area que será escrito o texto
    text_area = driver.find_element(By.CSS_SELECTOR, 'textarea#textbox')
    text_area.send_keys(texto)

    # clica no botão de submit após ter escrito na text_area
    # foi utilizado JS para clicar ao invés do element.click()    
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button#createTxt')
    driver.execute_script("arguments[0].click();", submit_button)

    # só então o botão de download aparece e podemos clicar nele
    download_button = driver.find_element(By.CSS_SELECTOR, 'a#link-to-download')
    driver.execute_script("arguments[0].click();", download_button)

    # é necessário esperar para garantir que o arquivo foi baixado
    sleep(7)

    # pega o caminho do arquivo baixado, que tem nome info.txt
    txt_file_path = os.path.join(output_dir, 'info.txt')

    driver.quit()
    return txt_file_path

def convertToPDF(txt_file_path):
    # função que irá receber o caminho do arquivo .txt e realiza a conversão dele para PDF

    # lê o arquivo .txt
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        texto = f.read()

    # inicializa o PDF, adicionando página e fonte
    pdf = FPDF()
    pdf.add_page()
    font_path = os.path.join(os.path.dirname(__file__), r'fonts\Sora-Regular.ttf')
    pdf.add_font("Sora", fname=font_path)
    pdf.set_font('Sora', size=14)

    # escreve no PDF, utilizando 0 para largura e 10 para altura da linha
    pdf.multi_cell(0, 10, texto)

    # baixa o arquivo PDF para a pasta destino
    output_dir = os.path.join(os.getcwd(), 'output')
    pdf_file_path = os.path.join(output_dir, 'output.pdf')

    pdf.output(pdf_file_path)

    return pdf_file_path

def main():
    # chama a função do selenium e depois a função para converter o .txt em PDF
    txt_file_path = launchBrowser()

    if os.path.exists(txt_file_path):
        pdf_file_path = convertToPDF(txt_file_path)
        print(f"O arquivo foi convertido com sucesso para PDF e está localizado em {pdf_file_path}")

if __name__ == "__main__":
    main()
