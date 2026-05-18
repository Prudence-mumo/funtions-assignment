def get_average(backend, frontend, design):
    return (backend + frontend + design) // 3

def get_grade(average):
    if average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'E'

def create_student_report(name, backend, frontend, design):
    average = get_average(backend, frontend, design)
    grade = get_grade(average)

    report = {
    'name': name,
    'Backend': backend,
    'Frontend': frontend,
    'Design': design,
    'average': average,
    'grade': grade
    }
    return report


name = input("Enter student name: ")
backend = int(input ("Enter Backend marks: "))
frontend = int(input ("Enter Frontend marks: "))
design = int(input ("Enter Design marks: "))

final_report = create_student_report(name, backend, frontend, design)

print (final_report)