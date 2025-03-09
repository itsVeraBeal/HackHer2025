#add a semester
def choose_semester():
    semesters = ['Fall','Winter']
    while True:
        semester = input('Choose a semester (Fall/Winter): ')
        if semester in semesters:
            return semester
        else:
            print('Invalid semester - Enter a valid semester (Fall/Winter)')

#add a course
def add_course():
    course_list = []
    while True:
        course = input("Enter course name: ")
        course_list.append(course)
        user = input("Add another course? (y/n): ")
        if user == 'n':
            break
    return course_list

#add an assessment
def add_assessment():
    grade_list = []
    while True:
        print('Enter assessment details: ')
        name = input('Assessment title: ')
        while True:
            grade = input('Number Grade: ')
            try:
                grade = float(grade)
                if grade >= 0 and grade <= 100:
                    break
                elif grade > 100:
                    print('Warning: Grade is greater than 100')
                    break
                else:
                    print('Grade must be a positive number')
            except:
                print('grade must be a number')
            
        while True:
            weight = input('Weight: ')
            try:
                weight = float(weight)
                if weight >= 0 and weight <= 100:
                    break
                else:
                    print('Weight must be a value between 0 and 100')
            except:
                print('weight must be a number')

        assessment = [name,grade,weight]
        grade_list.append(assessment)
        user = input('Add another assessment? (y/n): ')
        if user == 'n':
            break
    return grade_list

print('Semester: ',choose_semester())
print('Course List: ',add_course())
print('Assessment List: ',add_assessment())
