from flask import Flask
from flask import render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='82.156.172.44', port=5000, debug=True)


@app.route("/")
def hello_world():
    return render_template('index.html')
