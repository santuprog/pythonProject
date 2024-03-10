def calcuate_HCF(x,y):
    '''
    Objective: To find the highest common factor of two numbers. An HCF of x numbers is the largest number that can divide all x numbers with zero remainders.
    Input: num1, num2-- numberic numbers
    Return : HCF
    '''
    if x>y:
        h=y
    else:
        h=x
    while(True):
        if x%h==0 and y%h==0:
            hcf=h
            break
        else:
            h-=1
            continue
    return hcf

def main():
    '''
    Objective: To find the highest common factor of two numbers. An HCF of x numbers is the largest number that can divide all x numbers with zero remainders.
    Input: none
    Return : none
    '''
    x = int(input("Enter 1st Number: "))
    y = int(input("Enter 2nd Number: "))
    print("HCF is :", calcuate_HCF(x,y))

if __name__=='__main__':
    main()