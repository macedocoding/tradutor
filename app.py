import deepl
import requests
from bs4 import BeautifulSoup

auth_key = 'SUA CHAVE DE AUTENTICAÇÃO'
url = 'https://docs.powerembedded.com.br/portal-de-administracao/navegacao-do-portal'

response = requests.get(url)
pagina_html = response.text

soup = BeautifulSoup(pagina_html, 'html.parser')
html_limpo = soup.get_text(separator='\n')

translator = deepl.Translator(auth_key)
result = translator.translate_text(html_limpo, target_lang='EN-US')

with open('teste.txt', 'w', encoding='utf8') as f:
    f.write(str(result))
