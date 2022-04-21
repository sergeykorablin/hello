from flask import Flask
from markupsafe import escape
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route('/hello/<name>')
def hello(name):
    return f'Hello {escape(name)}'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
