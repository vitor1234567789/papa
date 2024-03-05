from flask import Flask, render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():
    nome = "vítor"  # escreva seu nome
    idade = "13"  # escreva sua idade
    return render_template('index.html', nome=nome, idade=idade)

# defina a rota para a página do pai
@app.route("/pai")
def pai():
    nome = "rafael"  # escreva seu nome
    idade = "43"  # escreva sua idade
    return render_template('index.html', nome=nome, idade=idade)

# defina a rota para a página da mãe
@app.route("/mãe")
def mae():
    nome = "natalia"  # escreva seu nome
    idade = "41"  # escreva sua idade
    return render_template('index.html', nome=nome, idade=idade)

# defina a rota para a página do amigo
@app.route("/irmã")
def irma():
    nome = "milena"  # escreva seu nome
    idade = "10"  # escreva sua idade
    return render_template('index.html', nome=nome, idade=idade)

# adicione outras rotas, se você quiser

# execute o arquivo
if __name__ == '__main__':
    app.run(debug=True)