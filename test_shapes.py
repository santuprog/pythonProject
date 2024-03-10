def triangle(n):
    k = 0
    count = 0

    for i in range(1, n + 1):
        for space in range(n-i,0,-1):
            print(" ", end=" ")
        for k in range(i,1,-1):
            print(k, end=" ")
        for j in range(1,i+1):
            print(j,end=" ")

        print()

def triangle1(n):
    for i in range (1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print(" ")

def empty_rectangle(n):
    for i in range(1,n+1):
        if i==1 or i==n:
            for j in range(1, n+1):
                print("*", end=" ")
        else:
            for j in range(1, n + 1):
                if j==1 or j==n:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print(" ")
def empty_triangle(n):
    for i in range (1,n+1):
        for j in range((n-i)+1,0,-1):
            print(" ", end=" ")
        for k in range(i,1,-1):
            print("*",end=" ")
        for l in range(1,i+1):
            print("*", end=" ")
        print()

def inverted_empty_triangle(n):
    for i in range (1,n+1):
        if i==1:
            for j in range(1,2*n+2):
                print("*",end=" ")
        else:
            for j in range(1,i):
                print(" ", end=" ")
            print("*", end=" ")
            for j in range(n,i,-1):
                print(" ", end=" ")
            for j in range(i,n+1):
                print(" ", end=" ")
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
    triangle(num)
    print(" ")
    triangle1(num)
    print(" ")
    empty_rectangle(num)
    print(" ")
    empty_triangle(num)
    print(" ")
    inverted_empty_triangle(num)

if __name__=="__main__":
    main()
