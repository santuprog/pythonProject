def title(str1):
    for x in range(len(str1)):
        if x==0:
            str2=str1[x].upper()
        elif x!=0 and str1[x-1]==' ':
            str2=str2+str1[x].upper()
        else:
            str2 = str2 + str1[x]

    return(str2)

def main():
    y=input("enter the sentence:")
    print(title(y))

if __name__=='__main__':
    main()