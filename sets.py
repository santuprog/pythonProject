def setfunction():
    '''note:
    set is an object type in pyhton. it is a comma separated unordered sequence of values enclosed within curly braces'''
    vowels=set('aeiou')
    print(vowels)
    '''
    Note: iterating over a set
    The order in which elements are printed when iterating over a Python set is not guaranteed. This is a fundamental characteristic of sets in Python'''
    for v in vowels:
        print(v, end=' ')

    '''
    Note:
    sets can be created from lists using set function over the list'''
    k=[10,20,30,40,50,9,5,44,66,789]
    m=set(k)
    print(m)

    '''
    note: 
    functions on set'''
    print(min(m))
    print(max(m))
    print(sum(m))
    print(len(m))
    '''
    note: 
    add function on set'''
    m.add(94)
    print(m)

    '''
    note: 
    update function on set'''
    m.update([45,65])
    print(m)

    '''
    note: 
    remove function on set'''
    m.remove(44)
    print(m)
    '''
    note: 
    pop function on set removes any arbitary value'''
    m.pop()
    print(m)
    '''
    note: 
    clear function on set'''
    m.clear()
    print(m)
    '''
    note: 
    union function on set'''
    fruits={'Apple','Orange','Tomato'}
    Vegetables={'Cucumber', 'Potato','Tomato'}
    eatables=fruits.union(Vegetables)
    print(eatables)
    eatables = fruits | Vegetables
    print(eatables)
    '''
    note: 
    intersection function on set'''
    fruitsandvegetables=fruits.intersection(Vegetables)
    print(fruitsandvegetables)
    fruitsandvegetables=fruits & Vegetables
    print(fruitsandvegetables)
    '''
    note: 
    difference function on set'''
    onlyfruits=fruits.difference(Vegetables)
    print(onlyfruits)
    onlyvegetables=Vegetables-fruits
    print(onlyvegetables)
    '''
    note: 
    XOR function on set to find only fruits or only vegetables '''
    fruitsXORvegetables=onlyfruits | onlyvegetables
    print(fruitsXORvegetables)
    fruitsXORvegetables=fruits.symmetric_difference(Vegetables)
    print(fruitsXORvegetables)
    '''
    note: 
    set.union, set.intersection, set.difference function on set to perform operation on multiple sets'''
    digit1={0,1,2,3}
    digit2={2,4,5,6}
    digit3={0,7,8,9,2}
    union_set=set.union(digit1,digit2,digit3)
    print(union_set)
    intersection_set=set.intersection(digit1,digit2,digit3)
    print(intersection_set)
    difference_set=set.difference(digit1,digit2,digit3)
    print(difference_set)
    '''
    note: 
    function copy on set '''
    digit4=digit1.copy()
    print(digit4)

    '''
    note: 
    subset and superset on set '''
    multiples2={2,4,6,8,10,12,14}
    multiples4={4,8,12}
    inSubset=multiples4<=multiples2
    print(inSubset)
    inSuperset = multiples2 >= multiples4
    print(inSuperset)
    '''
    note: 
    finding common factors on set '''
    n1=int(input("Enter the first value:"))
    n2=int(input("Enter the second value:"))
    commonFactors={i for i in range(1, min(n1+1,n2+1)) if n1%i==0 and n2%i==0}
    print(commonFactors)


def main():
   setfunction()

if __name__ == '__main__':
   main()