def main():
    '''
           to compute sum of numbers entered by the user until user provides null string as input
           input parameters: none
           return value : none
        '''
    total=0
    numbers=input("Enter a number: ")
    while numbers != '' :
        total += int(numbers)
        numbers=input("Enter a number: ")
    print("sum of numbers is", total)

if __name__=="__main__":
    main()