def printsquares():
    '''
                Objective: To print quares of positive numbers entered by the user. The program terminates if the user enters null string.
                input parameters: none
                return value : none
    '''

    while True:
        numString=input('enter the integer, to end press enter: ')
        if numString=='':
            break
        number =int(numString)
        print(number, '^ 2 =', number ** 2)
    print("End of Input!!")

def main():
    printsquares()

if __name__=='__main__':
    main()