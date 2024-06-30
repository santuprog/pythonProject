def wordcount(str1):
    y=len(str1.split())
    return y
def main():
    y=input("enter the sentence:")
    print(wordcount(y))

if __name__=='__main__':
    main()
