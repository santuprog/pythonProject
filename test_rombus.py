def rombus(n):
    for i in range (1,n):
        if i==1:
            for j in range(1, n+1):
                print(" ", end="")
            print("*")
        else:
            for j in range(n, i, -1):
                print(" ", end="")
            print("*", end="")
            for j in range(2, 2 * i + 1):
                print("*", end="")
            print("*", end="")
            print("")

    for i in range (1,n):
        for j in range(1,i):
            print(" ", end="")
        print("*", end="")
        for j in range(n,i,-1):
            print("*", end="")
        for j in range(i,n+1):
            print("*", end="")
        print("*", end="")
        print("")
    for i in range(1,n+2):
        if i<=n:
            print(" ", end="")
        else:
            print("*",end="")
    print("")

def main():
    num=int(input("enter number of rows "))
    rombus(num)

if __name__=="__main__":
    main()
