def remove_duplicates_uniquelist(list1):
    '''Create blank unique list then enter the values that are not inte unique list stating from the first value'''
    y=[]

    for i in list1:
        if i not in y:
            y.append(i)
    return y

def remove_duplicates_set(list1):
    '''create a set from the existing list ten convert it to list, since set does not contain duplicates'''
    y=list(set(list1))

    return y
def remove_duplicates_dictionsry(list1):
    '''using dictionary to deduplicate list '''
    y={}
    z=[]
    for i,x in enumerate(list1):
        y[x]=y.get(x,0)+1
        if y[x]>1:
            y[x]-=1
        else:
            z.append(x)

    return z




def main():
    list1=list(input('Enter the list of values separated by spaces: ').split())
    print("List entered by user is",list1)
    print("deduplicated list is: ",remove_duplicates_uniquelist(list1))

    print("deduplicated list is: ", remove_duplicates_set(list1))

    print("deduplicated list is: ", remove_duplicates_dictionsry(list1))

if __name__ == '__main__':
    main()