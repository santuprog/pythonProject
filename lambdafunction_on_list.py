def lambda_function():
    x=[10,20,30,40]
    '''  
    Note:
     map is used to transform all values of an iterable object
     lambda expression is used so that we dont have to define a new function to operate on the iterable object, in this case the list
    Note:
        below the square function is already defined so lambda expression is not required'''
    cube=list(map(lambda z: z ** 3,x))
    sqr=list(map(square,x))

    print(sqr)
    print(cube)

def square(y):
    return y**2

def main():
    lambda_function()

if __name__=='__main__':
    main()