from flask import Flask, render_template


app = Flask(__name__)
#changes

@app.route("/")
def index_page():
   message = 'Добро пожаловать! v2'
   url ='https://banner2.cleanpng.com/20190612/qbz/kisspng-github-pages-computer-icons-computer-software-github-logo-media-social-icon-5d007ece2bd8d3.7097023515603135501796.jpg'
   return render_template('index.html', message=message, url=url)
