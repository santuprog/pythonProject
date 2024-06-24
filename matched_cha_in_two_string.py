def nMatchedChar(string1,string2):
    temp1=string1.lower()
    temp2=string2.lower()

    count=0
    for s in temp1:
        for k in temp2:
            if s==k:
                count+=1
    return count

def main():
    string1=input('Enter 1st string:')
    string2=input('Enter 2nd string:')
    print('Matched charaters in the two strings are:',nMatchedChar(string1,string2))

if __name__=='__main__':
    main()