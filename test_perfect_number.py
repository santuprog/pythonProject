def perfect_number():
    '''
    Objective: to grade marks
    Input: none
    Return : none
    '''
    x=int(input("Enter a natural numbers: "))
    i=1
    n = []
    total=0
    while i<x:
        if x%i==0:
            n.append(i)
            i+=1
        else:
            i+=1
            continue
    for i in range(0,len(n)):
        total+=n[i]
    if total==x:
        print(total," is a perfect number", )
    else:
        print(x,"is not a perfect number")
def main():
    '''
    Objective: to grade marks
    Input: none
    Return : none
    '''
    perfect_number()

if __name__=='__main__':
    main()