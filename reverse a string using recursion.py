def reverse(str1):
    if str1=='':
        return str1
    else:
        return reverse(str1[1:])+str1[0]

def main():
    string1=input('Enter 1st string:')
    print('Matched charaters in the two strings are:',reverse(string1))

if __name__=='__main__':
    main()