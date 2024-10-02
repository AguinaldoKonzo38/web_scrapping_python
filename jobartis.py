import requests
from bs4 import BeautifulSoup
import math

# informatica-e-ti #?page=2&q%5Brequired_general_specializations_id_eq%5D=29
url_base = 'https://www.jobartis.com/vagas-emprego/'

# https://www.jobartis.com/vagas-emprego/gestor?page=100


def search_keyword(key):
    r_url = requests.get(f'{url_base}{key}?')
    html = r_url.text
    akak = BeautifulSoup(html, "html.parser")

    todos_trabalhos = akak.find('h5', class_='subheader mt-0').text
    # print('pegou total de vagas: '+todos_trabalhos)
    spitar_lista = todos_trabalhos.strip().split(' ')
    # print(spitar_lista)
    pagina_para_scrapp = math.ceil(int(spitar_lista[0])/20)

    urls = []
    for n_page in range(1): #pagina_para_scrapp):
        url = f"{url_base}{key}?page={1*(n_page)}"
        # print(url)
        urls.append(url)
    return scrapping_jobartis(urls)

    '''page_links = akak.find('ul', class_='pagination').find_all('li')

    numero_de_pagina = [0]
    for link in page_links:
        n_pagina = link.get_text()
        numero_de_pagina.append(n_pagina)
    # return numero_de_pagina

    urls = []
    for n_page in numero_de_pagina[:-1]:
        url = f"{url_base}{key}?page={1*(n_pagina)}"
        urls.append(url)
    return urls'''


def scrapping_jobartis(urls):
    todas_vagas = []
    for url in urls:
        print('Começando uma url...')
        r_url = requests.get(url)
        html = r_url.text
        # print(r_url.status_code)
        soup = BeautifulSoup(html, "html.parser")
        # print(soup)

        table = soup.find_all('div', class_='job')
        # print(table)
        for card in table:"https://jobartis.com"
            vaga = {
                'Title': card.find('h2').string,
                'Company': card.find('h5').string,
                'Location': card.find('li').string,
                'Tempo': card.find('p').get_text(),
                'Link': card.find('a').get('href'),
            }
            todas_vagas.append(vaga)
    return todas_vagas
