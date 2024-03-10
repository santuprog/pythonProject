def mySine(x):
    '''
    Objective: to fins the sum of sine series until the absolute value of newTerm becomes smaller than epsilon
    Input: x --numeric value of radius
    Return : total
    '''

    epsilon=0.00001
    multby= -x**2
    term=x
    total=x
    nxtInSeq= 2.0
    while abs(term) > epsilon:
        divby=(nxtInSeq*(nxtInSeq+1))
        term=(term*multby/divby)
        total=(total+term)
        nxtInSeq=(nxtInSeq+2)


    return total

def main():
    '''
    Objective: to fins the sum of sine series until the absolute value of newTerm becomes smaller than epsilon
    Input: none
    Return : total
    '''
    x=int(input("enter radius of the circle : "))
    print("Sum f sine series is : ", mySine(x))

if __name__=='__main__':
    main()