from flask import Flask, render_template, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')
Scss(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
