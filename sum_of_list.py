def sum_of_list(list1):
    x=[]
    sum=0
    for i in list1:
        sum+=int(i)
        x.append(sum)
    return x

def main():
    list1=list(input("Enter comma separated values of list: ").split(','))
    print("Input list is: ",list1)
    print("output list is: ",sum_of_list(list1))


if __name__=='__main__':
    main()