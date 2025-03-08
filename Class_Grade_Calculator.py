grade_list = [["midterm", 76, 30], ["final", 68, 70]]
class_grades = []

def number_grade_calculator(grade_list):
    class_grade = 0
    total_percent = 0
    for grade in grade_list:
        total_percent += grade[2]

    for grade in grade_list:
        num_grade = grade[1]
        weight = grade[2]
        class_grade += num_grade * (weight/total_percent)


    print(round(class_grade))

    return class_grade


def letter_grade_calculator(grade): #This will change to self.grade when we implement it with classes
    if  grade >= 90:
        letter_grade = "A+"
        class_gpa = 4.3
    elif 89 >= grade >= 85:
        letter_grade = "A"
        class_gpa = 4.0
    elif 84 >= grade >= 80:
        letter_grade = "A-"
        class_gpa = 3.7
    elif 79 >= grade >= 77:
        letter_grade = "B+"
        class_gpa = 3.3
    elif 76 >= grade >= 73:
        letter_grade = "B"
        class_gpa = 3

    elif 72 >= grade >= 70:
        letter_grade = "B-"
        class_gpa  = 2.7

    elif 69 >= grade >= 67 :
        letter_grade = "C+"
        class_gpa = 2.3

    elif 66 >= grade >= 63:
        letter_grade = "C"
        class_gpa = 2

    elif 62 >= grade >= 60:
        letter_grade = "C-"
        class_gpa = 1.7

    elif 59 >= grade >= 57:
        letter_grade = "D+"
        class_gpa = 1.3

    elif 56 >= grade >= 53:
        letter_grade = "D"
        class_gpa = 1

    elif 52 >= grade >= 50:
        letter_grade = "D-"
        class_gpa = 0.7

    elif grade < 50:
        letter_grade = "F"
        class_gpa = 0

    print(letter_grade)
    print(class_gpa)
    #Assign the letter grade and the class gpa to the class once incorporated to the other code.



class_grade = number_grade_calculator(grade_list)

class_grades.append(class_grade)
letter_grade_calculator(class_grade)