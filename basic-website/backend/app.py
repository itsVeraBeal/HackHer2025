from flask import Flask, render_template

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)