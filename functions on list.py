def main():
    # convert string to a list
    x=input("Enter the string: ")
    print(list(x))

    # append data to an existing list
    x=(input("Enter the values in the list: ").split(','))
    #this will accept the input as string values for a list
    print(x)
    y=int(input('Enter the new value: '))
    x.append(y)
    print(x)

    #extend accepts a sequence of argulaments then adds them to the list from the end
    z=input("Enter the sequence: ")
    z = list(map(int,z.split(',')))
    # this is used to insert the values in the list as integers
    x.extend(z)
    print(x)

    #count fumction counts the number of occurences of the object passed as an argument in the list
    a=[78,96,41,63,67,56,74,96,78]
    print(a.count(78))

    #pop return the element from the list whose index is passed as an argument
    print(a.pop(3))
    print(a)

    # remove removes the first occurence of an element passed as an argument from the list
    a.remove(78)
    print(a)
    
    #index funtion can tell us what is the index of a given value
    name=['Ram','Sham','Shiv','Vishnu','Bramha']
    roll=[1,2,3,4,5]
    roll.pop(name.index('Vishnu'))
    name.remove('Vishnu')
    print(name,'\n',roll)

    #del function removes a sequence from the list
    a = [78, 96, 41, 63, 67, 56, 74, 96, 78]
    del a[2:6:2]
    print(a)

    #insert function can be used to insert an object at a specified index
    names=['Ram','Sham','Shiv','Vishnu','Bramha']
    names.insert(2,'Ganesh')
    print(names)

    #reverse functions reverses the order of the elements in the list
    names.reverse()
    print(names)

    #sort function can be used to arrrage the elements of a list in ascending order
    names.sort()
    print(names)

    #for descensing order we need to add reverse=True as argument
    names.sort(reverse=True)
    print(names)

    #for sorting the values in a list as a key value obtained by using a function we need to pass key = function as argument
    names.sort(key=len)
    print(names)
    names.sort(key=ascii)
    print(names)



if __name__=='__main__':
    main()

