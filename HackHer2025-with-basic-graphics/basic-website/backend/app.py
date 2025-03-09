from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')



@app.route('/add_assignment', methods=['POST'])
def add_assignment():
    assignment_name = request.form['assignment_name']
    # Handle the assignment name (e.g., save to database)
    return redirect(url_for('index'))

@app.route('/add_grade', methods=['POST'])
def add_grade():
    grade = request.form['grade']
    # Handle the grade (e.g., save to database)
    return redirect(url_for('index'))

@app.route('/add_weight', methods=['POST'])
def add_weight():
    weight = request.form['weight']
    # Handle the weight (e.g., save to database)
    return redirect(url_for('index'))

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)