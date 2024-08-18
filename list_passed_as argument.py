def list_update(a,i,val):
    a[i]=val
    ''' Here a is a list , i is the index and value is the value that will need to be replaced with.
    Note that a points to the list lst. Since it is pointting to the same list so any change in a will result in a change in lst
    Both a and lst are reference to a set of values(objects) which is a list'''

def main():
    lst=[10, 20, 30, 40, 50]
    list_update(lst,1,90)
    print(lst)

if __name__=='__main__':
    main()