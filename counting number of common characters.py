def nCommonChars(str1,str2):
    temp1=str1.lower()
    temp2=str2.lower()

    count=0
    for i in range(len(temp1)):
        ch1=temp1[i]
        if not (ch1 in temp1[:i]):
            for ch2 in temp2:
                if ch1==ch2:
                    count+=1
                    break
    return count

def main():
    string1=input('Enter 1st string:')
    string2=input('Enter 2nd string:')
    print('Matched charaters in the two strings are:',nCommonChars(string1,string2))

if __name__=='__main__':
    main()