from flask import render_template
from flask import Flask
from gevent import pywsgi

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


server = pywsgi.WSGIServer(('0.0.0.0', 4000), app)
server.serve_forever()
