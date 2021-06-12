from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=('POST', 'GET'))
def index():
    nome = None
    sobrenome = None
    classe = None
    escolha_imagem = None

    if request.method == "POST":
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        classe = request.form['classe']

    if classe == 'elfo':
        escolha_imagem = 'https://i.pinimg.com/originals/52/b8/c3/52b8c320e93e722020f51d6e4920d6bc.gif'
    elif classe == 'orc':
        escolha_imagem = 'https://thumbs.gfycat.com/ExemplarySeriousBeardedcollie-max-1mb.gif'
    elif classe == 'hobbit':
        escolha_imagem = 'https://media.tenor.com/images/a758b5c5a136dde219fc5926b42c7b1b/tenor.gif'

    return render_template(
        "index.html",
        nome=nome,
        sobrenome=sobrenome,
        classe=classe,
        escolha_imagem=escolha_imagem
    )


if __name__ == "__main__":
    app.run(debug=True)
