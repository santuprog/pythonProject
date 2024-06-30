def func(str1):
    temp1=str1
    x=''

    for i in range(len(temp1)):
        ch1=temp1[i]
        if ch1 not in temp1[:i]:
            x=x+ch1
        else:
            x=x+'*'
    print(x)

def main():
    y=input("enter the string:")
    func(y)

if __name__=='__main__':
    main()