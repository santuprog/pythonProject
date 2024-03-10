import random
x=random.random()+5
print(x)

y=pow(9,2)
print(y)

def rombus():
        print("      *      ")
        print("   *  *  *   ")
        print("*  *  *  *  *")
        print("   *  *  *   ")
        print("      *      ")

def square():
    print("$  $  $  $  $")
    print("$           $")
    print("$           $")
    print("$           $")
    print("$  $  $  $  $")

def nMultiple(a=0, num=1):
    return a*num

def test(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("a= ", a)
    print("b= ", b)

def func():
    pass

def main():
    rombus()
    print("\n")
    square()
    print("\n")
    print(nMultiple(5, num=7))
    test(5, 8)
    a=func()
    print(a)

if __name__=='__main__':
    main()

