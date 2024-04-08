from flask import Flask, render_template, url_for
from scraping import buscar_noticias_bahia_noticias 

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/sobremim')
def sobre_mim():
    return render_template('sobremim.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/processar_busca', methods=['POST'])
def processar_busca():
    url = 'https://www.bahianoticias.com.br/pesquisa/petrobras'
    dados_html = buscar_noticias_bahia_noticias(url)
    return render_template('input.html', dados_html)