def add_assessment():
    course_list = []
    while True:
        print('Enter assessment details: ')
        name = input('Assessment title: ')
        grade = int(input('Grade: '))
        weight = float(input('Weight: '))
        assessment = [name,grade,weight]
        course_list.append(assessment)
        user = input('Add another assessment? (y/n): ')
        if user == 'n':
            break
    return course_list
    
print(add_assessment())
