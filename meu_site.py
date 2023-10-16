from flask import Flask, render_template

app = Flask(__name__) # Comando padrão que cria o Site

#Criar Primeira Página
# Toda página tem o Route -> nicolas.com/contatos , Caminho depois do nome do dominio
# E uma Função -> O que voce quer exibir naquela página
# Template - Por padrão o HTML e CSS fica na pasta Template

@app.route("/") # Comando para definir o link, Linha de código que o objetivo é atribuir uma nova funcionalidade pra função abaixo
def homepage():
    return render_template("index.html")

if __name__ == "__main__": # Se não tiver essa linha de código vai dar erro no site no deploy
    app.run(debug = True) # Estamos criando o site e ativar o debugar do site, Vai aparecer as edições apenas dando F5

# Servidor do HEROKU