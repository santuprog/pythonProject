def inverted_right_triangle(n):
    for i in range(1,n+1):
        for j in range(i-1,0,-1):
            print(" ", end=" ")
        for j in range(n-i+1,0,-1):
            print("$", end=" ")

        print("")

def main():
    num=int(input("enter number of rows "))
    inverted_right_triangle(num)

if __name__=="__main__":
    main()

