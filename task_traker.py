from flask import Flask, render_template

class Task():
    def __init__(self, nome, data_ini, status, data_upd, descricao):
        self.nome = nome
        self.data_ini = data_ini
        self.status = status
        self.data_upd = data_upd
        self.descricao = descricao

app = Flask(__name__)

@app.route("/index")
def ola():
    task1 = Task('Python', '13/07/2025', 'in-progress', '13/07/2025', 'Aprendendo sobre flask')
    task2 = Task('sql', '13/07/2025', 'in-progress', '13/07/2025', 'Aprendendo CRUD')
    task = [task1, task2]
    return render_template('main.html', titulo='Task_Tracker' ,tasks= task)


app.run(debug=True)