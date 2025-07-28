from flask import Flask, render_template, request

class Task():
    def __init__(self, nome, data_ini, status, data_upd, descricao):
        self.nome = nome
        self.data_ini = data_ini
        self.status = status
        self.data_upd = data_upd
        self.descricao = descricao

task1 = Task('Python', '13/07/2025', 'in-progress', '13/07/2025', 'Aprendendo sobre flask')
task2 = Task('sql', '13/07/2025', 'in-progress', '13/07/2025', 'Aprendendo CRUD')
lista = [task1, task2]


app = Flask(__name__)

@app.route("/")
def index():

    return render_template('main.html', titulo='Task_Tracker' ,tasks= lista)

@app.route("/novo")
def novo():
    return render_template("novo.html", titulo = "New Task")

@app.route("/criar", methods= ['POST',])
def criar():
    nome = request.form['nome']
    data_ini = request.form['data_ini']
    status = request.form['status']
    data_upd = request.form['data_upd']
    descricao = request.form['descricao']
    task = Task(nome, data_ini, status, data_upd, descricao)

    lista.append(task)
    return render_template('main.html', titulo='Task_Tracker', tasks = lista)

app.run(debug=True)