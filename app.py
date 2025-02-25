from flask import Flask, render_template


app = Flask(__name__)
#changes

@app.route("/")
def index_page():
   message = 'Добро пожаловать! v2'
   return render_template('index.html', message=message)
