class CourseGrade:
    def __init__(self,assessment):
        self.assessment = assessment
    
    def show_grades(self):
        grade_list = []
        grade_list.append(assessment.add_grade())
        return grade_list

class Assessment:
    def __init__(self, name, grade, weight):
        self.name = name
        self.grade = grade
        self.weight = weight
    
    def add_grade(self):
        return [self.name, self.grade,self.weight]
    
print('Enter assessment details: ')
name = input('Assessment title: ')
grade = int(input('Grade: '))
weight = float(input('Weight: '))
assessment = Assessment(name,grade,weight)
all_grades = CourseGrade(assessment)
print(all_grades.show_grades())