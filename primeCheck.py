def prime(n):
    '''
    Objective: to check if a number is prime or not
    Input: n --numeric value
    Return : message --boolean value
    '''
    if n==1:
        return False
    for i in range(2,n):
        if n % i==0:
            Flag=False # n is not a prime
            break
    else:
        Flag=True # n is prime
    return Flag

def main():
    '''
    Objective: to check if a number is prime or not
    Input: none
    Return : none
    '''
    n=int(input('enter number to check if prime: '))
    result=prime(n)
    if result==True:
        print(n,'is a prime')
    else:
        print(n,'is not a prime')

if __name__=='__main__':
    main()
