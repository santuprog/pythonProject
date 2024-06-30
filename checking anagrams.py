def anagrams(str1, str2):
    count=len(str1)
    if len(str1)==len(str2):
        for ch1 in str1:
            for ch2 in str2:
                if ch1==ch2:
                    count=count-1
                    break
    if count==0:
        return True
    else:
        return False

def main():
    x=input("enter 1st string:")
    y = input("enter 2nd string:")
    print(anagrams(x,y))

if __name__=='__main__':
    main()