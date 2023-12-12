from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
      return render_template("Contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome=nome_usuario)

    if __name__ == "main":
        app.run(debug=True)