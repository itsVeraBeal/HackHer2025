import ClassGrade
import GradeList
from SemesterGrade import semester_grades
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Data Class ~ Row of data
class MyGrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"Grade {self.id}"

# Routes to Webpages
# Home page
@app.route('/', methods=["POST", "GET"])
def index():
    # Add a course
    if request.method == "POST":
        course_name = request.form['courseName']
        if course_name:
            new_course = MyGrade(courseName=course_name)
            try:
                db.session.add(new_course)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                print(f"Error: {e}")
                return f"Error: {e}"
        else:
            return "Course name is required"
    # See courses
    else:
        courses = MyGrade.query.all()
        return render_template('index.html', courses=courses)

# Delete a course
@app.route("/delete/<int:id>")
def delete(id: int):
    delete_course = MyGrade.query.get_or_404(id)
    try:
        db.session.delete(delete_course)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"Error: {e}"

# Grades page
@app.route("/grade/<int:id>", methods=["POST", "GET"])
def grades(id: int):
    course = MyGrade.query.get_or_404(id)
    if request.method == "POST":
        assessment_name = request.form['assessmentName']
        grade = request.form['grade']
        try:
            grade = int(grade)
            new_assessment = MyGrade(courseName=assessment_name, grade=grade)
            db.session.add(new_assessment)
            db.session.commit()
            return redirect(f'/grade/{id}')
        except Exception as e:
            return f"Error: {e}"
    else:
        assessments = MyGrade.query.filter_by(courseName=course.courseName).all()
        return render_template('grade.html', course=course, assessments=assessments)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
      
    app.run(debug=True)