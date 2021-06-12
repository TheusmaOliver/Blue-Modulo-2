from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        usuario_nome = request.form["usuario_nome"]
        usuario_sobrenome = request.form["usuario_sobrenome"]
        sexo = request.form["sexo"]
        skills = request.form["skills"]
        print(f'Nome: {usuario_nome}')
        print(f'Sobrenome: {usuario_sobrenome}')
        print(f'Sexo: {sexo}')
        print(f'Skills: {skills}')

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
