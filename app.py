from flask import Flask, render_template, url_for
from scraping import dados_html 

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
def dinamica():
    return render_template('dinamica.html',dados_html=dados_html)

@app.route('/processar_busca', methods=['POST'])
def processar_busca():
    url = 'https://www.bahianoticias.com.br/pesquisa/petrobras'
    return render_template('dinamica.html', dados_html=dados_html)