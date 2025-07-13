from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def ola():
    return render_template('main.html', titulo='Task_Tracker')


app.run(debug=True)