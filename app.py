from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobremim')
def sobre_mim():
    return render_template('sobremim.html')

@app.route('/portifolio')
def portfolio():
    return render_template('portifolio.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
    python app.py