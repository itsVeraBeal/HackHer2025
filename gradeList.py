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
        grade = int(input('Grade: '))
        weight = float(input('Weight: '))
        assessment = [name,grade,weight]
        grade_list.append(assessment)
        user = input('Add another assessment? (y/n): ')
        if user == 'n':
            break
    return grade_list

print('Semester: ',choose_semester())
print('Course List: ',add_course())
print('Assessment List: ',add_assessment())
