import functools


def lambda_function():
    x=[1,3,6,20,30,40, 9993]
    '''  
    Note:
     map is used to transform all values of an iterable object
     lambda expression is used so that we dont have to define a new function to operate on the iterable object, in this case the list'''

    cube=list(map(lambda z:z ** 3,x))
    '''    Note:
        below the square function is already defined so lambda expression is not required'''
    sqr=list(map(square,x))
    x=[-1,8,-22,9,-55]
    absolute=list(map(abs,x))
    '''Note: 
    adding elements of an iterable object is a repetative procedure and function reduce available in module functools can be used to do this'''

    sumcubes=functools.reduce(lambda k,y :y+k, cube)

    '''Note: 
    the filter function takes a function and an iterable object as parameters and returns only those elements from the iterable object '''

    evenCube=list(filter(lambda x: x%2==0,cube))
    sumEvenCubes=functools.reduce(lambda x,y: x+y,evenCube)

    print(sqr)
    print(cube)
    print(absolute)
    print(sumcubes)
    print(evenCube)
    print(sumEvenCubes)
def square(y):
    return y**2

def main():
    lambda_function()

if __name__=='__main__':
    main()