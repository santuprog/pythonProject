def reverse(str1):
    reverse_str=''
    for i in range(len(str1)):
        reverse_str=str1[i]+reverse_str
    return reverse_str


def main():
    string1=input('Enter 1st string:')
    print('Matched charaters in the two strings are:',reverse(string1))

if __name__=='__main__':
    main()