from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Získání GET parametrů z URL
    decoration = request.args.get('decoration', 'all')
    
    return render_template("index.html", decoration=decoration)