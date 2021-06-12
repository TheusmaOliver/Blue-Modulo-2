from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    name = "Sasuke"
    hp = 1500

    exibir_imagem = True
    imagem = "https://thumbs.gfycat.com/EnlightenedSimplisticCobra-size_restricted.gif"

    return render_template(
        "index.html",
        name=name,
        hp=hp,
        exibir_imagem=exibir_imagem,
        imagem=imagem
    )


@app.route('/personagem2')
def personagem2():
    name = "Naruto"
    hp = 2000

    exibir_imagem = True
    imagem = "https://i.gifer.com/origin/4b/4b55a5c5f95757c8d56c089051fa21f7_w200.gif"

    return render_template(
        "personagem2.html",
        name=name,
        hp=hp,
        exibir_imagem=exibir_imagem,
        imagem=imagem
    )


if __name__ == "__main__":
    app.run(debug=True)
