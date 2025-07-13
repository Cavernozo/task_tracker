from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def ola():
    return "<h1>Ola,mundo</h1>"

app.run(debug=True)