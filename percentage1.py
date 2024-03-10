def main():
    '''
                    Objective: to display percentage of marks scored by students
                    input parameters: none
                    return value : none
    '''

    totalMarks=0
    nSubjects=0 
    while True:
        marks= input('marks for subject' + str(nSubjects +1) + ': ')
        if marks== '':
            break
        marks = float(marks)
        if marks < 0 or marks > 100:
            print('INVALID MARKS!!')
            continue
        nSubjects= nSubjects+1
        totalMarks +=marks
    percentage = totalMarks/nSubjects
    print('Total marks: ', int(totalMarks))
    print('number of subjects: ', nSubjects)
    print('Percentage: ', percentage)

if __name__=='__main__':
    main()
