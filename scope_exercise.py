a=4
def f():
    a=5
    def g():
        nonlocal a
        a=10
        print("inside g value of a=", a)
        def h():
            nonlocal a
            a=20
            print("inside h value of a=",a)
        h()
    g()
    print("inside f value of a=", a)
print("outside f value of a=", a)

def main():
    f()
if __name__=="__main__":
    main()