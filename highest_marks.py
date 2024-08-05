def main():
    marklist=[78,88,55,93,98,77]
    count=0
    for marks in marklist:
        if marks>=75:
            count+=1
    print('The marks list1 count is: ',count)
#using input from user
    marklist=eval(input('Enter the marks list: '))#enter square brackets when entering the values
    count=0
    for marks in marklist:
        if marks>=75:
            count+=1
    print('The marks list2 count is: ',count)

if __name__=='__main__':
    main()