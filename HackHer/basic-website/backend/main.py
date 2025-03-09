import ClassGrade
import GradeList
from SemesterGrade import semester_grades

#USER TESTING

semester = GradeList.choose_semester()
course = GradeList.add_course()
grade_list = GradeList.add_assessment()
average = ClassGrade.number_grade_calculator(grade_list)
avg = ClassGrade.letter_grade_calculator(average)


semester = semester_grades([["Cisc 102", 83, "A", 4], ["Math 121", 75, "B", 3.5], ["Cisc 121", 78, "B+", 3.7]])
semester_grades.culmulative_gpa(semester)

#print(semester_grades.number_gpa(semester))