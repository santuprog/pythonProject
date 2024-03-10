def multiplication_table(n, multiple):
    '''
       to print multiplication table of a user defined number
       input parameters: n - numeric value, multiple numeric value
       return value : none
    '''

    result=0
    for count in range(1,multiple+1):
        result=n*count
        print(n,"*","%2d"%count,"=","%2d"%result)

def main():
    '''
           to print multiplication table of a user defined number
           input parameters: none
           return value : none
    '''
    multiple = int(input("Upto which multiple you need the multiplication table? "))
    n=int(input("Which number do you want the multiplication table for? "))
    multiplication_table(n, multiple)

if __name__=='__main__':
    main()
