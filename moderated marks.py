def moderate(marks,passmarks):
    if marks==passmarks-1 or marks==passmarks-2:
        marks=passmarks
    return marks

def main():
    passmarks=40
    marks=input("enter marks: ")
    intmarks=int(marks)
    moderatedMarks=moderate(intmarks, passmarks)
    print("Moderated marks: ", moderatedMarks)

if __name__=="__main__":
    main()

