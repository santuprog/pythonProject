def wordcount(str):
    x=str.count(' ')
    x=x+1

    return x

def main():
    y=input("enter the sentence:")
    print(wordcount(y))

if __name__=='__main__':
    main()

