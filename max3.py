import pdb
pdb.set_trace()

def max3(x1,x2,x3):
    maxnumber=0
    if x1>x2:
        if x2>x3:
            maxnumber=x1
    elif x2>x3:
        maxnumber=x2
    else:
        maxnumber=x3
    return maxnumber

def main():
    x1=int(input("enter 1st number: "))
    x2=int(input("enter 2nd number: "))
    x3=int(input("enter 3rd number: "))
    max=max3(x1,x2,x3)
    print(max)

if __name__=="__main__":
    main()