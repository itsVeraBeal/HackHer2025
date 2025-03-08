class semester_grades:
    def __init__ (self, class_list):
        self.class_list = class_list
        self.gpa = 0
        self.num_gpa = 0

    #Let classlist be in the form of [[classname, numbergrade, lettergrade, class_gpa], [classname, numbergrade, lettergrade, class_gpa]]
    def culmitive_gpa(self):
        total = 0
        for grade in self.class_list:
            total += grade[3]

        self.gpa = round((total/len(self.class_list)), 2)
        print(self.gpa)
        return self.gpa

    def number_gpa(self):
        total = 0
        for grade in self.class_list:
            total += grade[1]

        self.num_gpa = round(total/len(self.class_list))

        print(self.num_gpa)
        return(self.num_gpa)
semester = semester_grades([["Cisc 102", 83, "A", 4], ["Math 121", 75, "B", 3.5], ["Cisc 121", 78, "B+", 3.7]])

semester_grades.culmitive_gpa(semester)
semester_grades.number_gpa(semester)
