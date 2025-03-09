grade_list = [["midterm", 76, 30], ["final", 68, 70]]
class_grades = []

class class_grade: 
    def __init__ (self, grade_list,): 
        self.grade_lit = grade_list
        self.name  = 
    def number_grade_calculator(grade_list):
        class_grade = 0
        total_percent = 0
        for grade in grade_list:
            total_percent += grade[2]

        for grade in grade_list:
            num_grade = grade[1]
            weight = grade[2]
            class_grade += num_grade * (weight/total_percent)
            task_letter_grade = None
            #Calculates the letter grade:
            if grade[1] >= 90:
                letter_grade = "A+"
            elif 89 >= grade[1] >= 85:
                task_letter_grade = "A"
            elif 84 >= grade[1] >= 80:
                task_letter_grade = "A-"
            elif 79 >= grade[1] >= 77:
                task_letter_grade = "B+"
            elif 76 >= grade[1] >= 73:
                task_letter_grade = "B"

            elif 72 >= grade[1] >= 70:
                task_letter_grade = "B-"

            elif 69 >= grade[1] >= 67:
                task_letter_grade = "C+"

            elif 66 >= grade[1] >= 63:
                task_letter_grade = "C"

            elif 62 >= grade[1] >= 60:
                task_letter_grade = "C-"

            elif 59 >= grade[1] >= 57:
                task_letter_grade = "D+"

            elif 56 >= grade[1] >= 53:
                task_letter_grade = "D"

            elif 52 >= grade[1] >= 50:
                task_letter_grade = "D-"

            elif grade[1] < 50:
                letter_grade = "F"

            print (grade[0])
            print(task_letter_grade)

        print(round(class_grade))
        letter_grade_calculator(class_grade)
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

        grade 
        print(letter_grade)
        print(class_gpa)
        grade = 
        #Assign the letter grade and the class gpa to the class once incorporated to the other code.

    def remove_grade(grade_list, remove_target):
        target = grade_list[remove_target]
        grade_list.remove(target)




    class_grade = number_grade_calculator(grade_list)

    class_grades.append(class_grade)
    letter_grade_calculator(class_grade)