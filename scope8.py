def f():
    print('global f')
def g():
    global f
    print('Before redefinition of f:, id(f): ', id(f))
    def f():
        print('inner f')
    print('after redefinition of f: id(f):', id(f))
    f()


def fprime():
    pass


def h():
    print('Inside h: id(f)', id(f))
    f()
    fprime()

def main():
    print('in global namespace: id(f):', id(f))
    fprime=f
    f()
    h()
    g()
    print('in global namespace: id(f): ', id(f))
    fprime()
   #h()
if __name__=='__main__':
    main()
