def inverted_isosceles_triangle(n):
    for i in range (1,n+1):
        if i==1:
            for j in range(1,2*n+2):
                print("*",end=" ")
        else:
            for j in range(1,i):
                print(" ", end=" ")
            print("*", end=" ")
            for j in range(n,i,-1):
                print("*", end=" ")
            for j in range(i,n+1):
                print("*", end=" ")
            print("*", end=" ")
        print("")
    for i in range(1,n+2):
        if i<=n:
            print(" ", end=" ")
        else:
            print("*",end=" ")
    print("")


def main():
    num=int(input("enter number of rows "))
    print(" ")
    inverted_isosceles_triangle(num)

if __name__=="__main__":
    main()
