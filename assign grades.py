def assignGrades(marks):
    '''
    to assign grades to students based on marks
    input parameters: marks- numeric value
    return value : grades - string
    '''
    assert marks>=0 and marks<=100
    if marks>=90:
        grade='A'
    elif 70<=marks<90:
        grade='B'
    elif 50<=marks<70:
        grade='C'
    elif 40<=marks<50:
        grade='D'
    else:
        grade='F'
    return grade

def main():
    '''
    to assign grades to students based on marks
    input parameters: none
    return value: none
    '''
    marks=float(input('Enter marks of the student: '))
    print(assignGrades(marks))

if __name__=="__main__":
    main()

