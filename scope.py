a=4
def f():
    a=5
    def g():
        nonlocal a
        print("inside functiog g, a= ", a)
        a=10
        print("inside functiog g after value change, a= ",a)
        def h():
            nonlocal a
            a=20
            print("inside function h, a= ", a)
        h()
    g()
    print("inside function f, a= ", a)
f()
print("outside all function, a= ", a)
