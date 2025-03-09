class semester_grades:
    def __init__ (self, class_list):
        self.class_list = class_list
        self.gpa = 0
        self.num_gpa = 0

    #Let classlist be in the form of [[classname, numbergrade, lettergrade, class_gpa], [classname, numbergrade, lettergrade, class_gpa]]
    def culmulative_gpa(self):
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
