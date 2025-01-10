from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "CHAVE_SECRETA_ALEATORIA"

@app.route("/")
def index():
    """
    Rota inicial: zera a pontuação e redireciona para a primeira pergunta.
    """
    session["score"] = 0
    return render_template("index.html")

@app.route("/pergunta1", methods=["GET", "POST"])
def pergunta1():
    """
    Página da primeira pergunta.
    Se for GET, renderiza o template. 
    Se for POST, verifica a resposta e atualiza a pontuação.
    """
    if request.method == "POST":
        resposta = request.form.get("resposta")
        # Por exemplo, a resposta correta poderia ser "2" (se você enumerar as opções)
        # Ou poderia ser "Brasília", depende de como você montar o HTML.
        # Aqui supomos que estamos comparando com "1", "2", "3", "4", etc.
        if resposta == "1":  
            # Se for a opção correta
            session["score"] += 1
        
        # Independente de acertar ou errar, segue para a pergunta2
        return redirect(url_for("pergunta2"))
    
    return render_template("pergunta1.html")


@app.route("/pergunta2", methods=["GET", "POST"])
def pergunta2():
    """
    Página da segunda pergunta.
    """
    if request.method == "POST":
        resposta = request.form.get("resposta")
        # Verifique qual opção é correta
        if resposta == "3":
            session["score"] += 1
        return redirect(url_for("pergunta3"))
    
    return render_template("pergunta2.html")


@app.route("/pergunta3", methods=["GET", "POST"])
def pergunta3():
    """
    Página da terceira pergunta.
    """
    if request.method == "POST":
        resposta = request.form.get("resposta")
        # Verifique qual opção é correta
        if resposta == "2":
            session["score"] += 1
        return redirect(url_for("resultado"))
    
    return render_template("pergunta3.html")


@app.route("/resultado")
def resultado():
    """
    Exibe a pontuação final.
    """
    pontuacao_final = session.get("score", 0)
    return render_template("resultado.html", pontuacao=pontuacao_final)


if __name__ == "__main__":
    app.run(debug=True)
