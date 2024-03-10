def maximum3(n1,n2,n3):
    '''
    to find maximum of 3 numbers
    input parameters: 3 numbers- numeric value
    return value : maxumum number - numeric value
    '''
    if n1>n2:
        if n1>n3:
            maxnumber=n1
        else:
            maxnumber=n3
    else:
        if n2>n3:
            maxnumber=n2
        else:
            maxnumber=n3
    return maxnumber
def main():
    '''
    to find maximum of 3 numbers
    input parameters: none
    return value: none
    '''
    n1=float(input('Enter first number: '))
    n2 = float(input('Enter second number: '))
    n3 = float(input('Enter third number: '))
    print(maximum3(n1,n2, n3))

if __name__=="__main__":
    main()

