def lowest_common_multiple(num1, num2):
    '''
    Objective: To find the Lowest common multiple of two numbers. An LCM of x numbers is the smallest number that can be divided with zero remainders by the x given numbers. It is used to d
    Input: num1, num2-- numberic numbers
    Return : LCM
    :return:
    '''
    multiple1=[]
    multiple2=[]
    for i in range (1,num1*num2+1):
        if i%num1==0:
            multiple1.append(i)
            if i%num2==0:
                multiple2.append(i)
            else:
                continue
        elif i%num2==0:
            multiple2.append(i)
        else:
             continue
    print(multiple1,"\n", multiple2)
    for i in range(1,len(multiple2)):
        for j in range(1,len(multiple1)):
            if multiple2[i]==multiple1[j]:
                return multiple2[i]
                break
            else:
                continue
def more_efficient_calculate_lcm(x, y):
    # selecting the greater number
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def main():
    '''
    Objective: To find the Lowest common multiple of two numbers. An LCM of x numbers is the smallest number that can be divided with zero remainders by the x given numbers. It is used to d
    Input: none
    Return : none
    :return:
    '''
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    print("LCM is :", lowest_common_multiple(num1, num2))

    x = int(input("Enter 1st Number: "))
    y = int(input("Enter 2nd Number: "))
    print("LCM is :", more_efficient_calculate_lcm(x, y))

if __name__=='__main__':
    main()

