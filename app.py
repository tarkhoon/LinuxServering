from flask import Flask, render_template


app = Flask(__name__)
#changes

@app.route("/")
def index_page():
   message = 'Добро пожаловать!'
   return render_template('index.html', message=message)
