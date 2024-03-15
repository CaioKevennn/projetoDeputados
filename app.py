from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

def get_deputados():
    response = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome')
    data = response.json()
    return data['dados']

@app.route('/')
def lista_deputados():
    return render_template('lista_deputados.html', deputados=get_deputados())

@app.route('/deputado/<int:id_deputado>')
def detalhes_deputado(id_deputado):
    response = requests.get(f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}')
    data = response.json()
    return render_template('detalhes_deputado.html', deputado=data['dados'])

if __name__ == '__main__':
    app.run(debug=True)
