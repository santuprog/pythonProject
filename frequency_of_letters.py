def frequency_of_letters(list1):
    x={}
    for i,e in enumerate(list1):
        x[e]=x.get(e,0)+1
    return x




def main():
    list1=list(input("Enter the sentence "))
    print(list1)
    print(frequency_of_letters(list1))



if __name__=='__main__':
    main()