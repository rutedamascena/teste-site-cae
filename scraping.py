import requests
import bs4
import pandas as pd

def buscar_noticias_bahia_noticias(url):
    requisicao = requests.get(url)
    html = requisicao.content
    sopa = bs4.BeautifulSoup(html, 'html.parser')
    
    clipping_bahianoticias = sopa.findAll('div', {'class': 'sc-3c754a49-0 edpZTL'})
    titulos = sopa.find_all('h3', {'class': 'sc-3c754a49-2 iihoil'})
    
    lista_titulos = []
    for titulo in titulos:
        lista_titulos.append(titulo.text.strip('...'))
    
    manchetes_link = []
    for noticia, titulo in zip(clipping_bahianoticias, titulos):
        link_ = 'https://www.bahianoticias.com.br' + noticia.find('a').get('href')
        titulo_ = titulo.text.strip('...')
        manchetes_link.append([titulo_, link_])
    
    bahia_noticias = pd.DataFrame(manchetes_link, columns=['Título', 'Link'])
    bahia_noticias['veículo'] = 'BAHIA NOTÍCIAS'
    
    return bahia_noticias

def dataframe_para_html(dataframe):
    # Converter DataFrame para HTML
    html = dataframe.to_html(index=False)  # index=False para não incluir o índice do DataFrame
    return html

url = 'https://www.bahianoticias.com.br/pesquisa/petrobras'
dados_noticias = buscar_noticias_bahia_noticias(url)
dados_html = dataframe_para_html(dados_noticias)
print(dados_html)  # Apenas para verificar a saída HTML no console