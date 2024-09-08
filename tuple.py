def tuple_operations():
    t1=('Monday', 'Tuesday')
    t2=(10,20,30)
    t3=('Jan','Feb','Mar','Apr','May','Jun')

    '''Multiplication'''
    print(t1*2)
    '''Concatenation'''
    print(t1+('Wednesday',))
    '''indexing'''
    print(t2[2])
    '''length'''
    len(t2)
    '''Slicing'''
    print(t3[2:5])
    '''min'''
    print(min(t2))
    '''max'''
    print(max(t2))
    '''sum'''
    print(sum(t2))
    '''membership'''
    print('Jan' in t3)

    '''functions on tuple'''
    t4=tuple('aeiou')
    print(t4)
    t5=tuple([4,10,22])
    print(t5)
    t6=tuple(range(10))
    print(t6)

    '''producing a list of tuples from elements of iterable object'''
    colours=('red','yellow','orange')
    fruits=['cherry','banana','orange']
    quantity=('1 kg',12, '2 kg')
    fruitcolour=list(zip(colours,fruits))
    print(fruitcolour)
    fruitscolorquantity=list(zip(fruitcolour,quantity))
    print(fruitscolorquantity)
    fruitcolourquantity=list(zip(colours,fruits,quantity))
    print(fruitcolourquantity)

    '''count in tuple'''
    t6=(10,20,30,40,10,60,70,60,50,10)
    print(t6.count(10))
    '''index function'''
    print(t6.index(10))




def main():
        tuple_operations()

if __name__ == '__main__':
        main()