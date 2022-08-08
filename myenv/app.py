from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cad/usuario")
def usuario():
    return render_template("user.html")


@app.route("/cad/caduser", methods=["POST"])
def caduser():
    return request.form

@app.route("/cad/anuncio")
def anuncio():
    return render_template("anuncio.html")

@app.route("/anuncios/pergunta")
def pergunta():
    return render_template("pergunta.html")

@app.route("/anuncios/compra")
def compra():
    return ""

@app.route("/anuncios/favoritos")
def favoritos():
    print("favorito inserido")
    return ""

@app.route("/config/categoria")
def categoria():
    return render_template("categoria.html")

@app.route("/relatorios/vendas")
def relVendas():
    return render_template("relVendas.html")

@app.route("/relatorios/compras")
def relCompras():
    return render_template("relCompras.html")