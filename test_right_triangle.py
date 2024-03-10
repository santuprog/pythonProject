def right_triangle(n):
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ", end=" ")
        for j in range(i,0,-1):
            print("*", end=" ")
        print("")

def main():
    num=int(input("enter number of rows "))
    right_triangle(num)

if __name__=="__main__":
    main()
