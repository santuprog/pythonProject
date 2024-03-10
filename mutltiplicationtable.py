def printTable(nMultiples=10, nTables=10) :
    '''
               To print multiplication table of numbers in range [1,nTable], comprising of first n multiples
               input parameters: nMultiples
                                nTables
               return value : none
            '''
    for multiples in range(1, nMultiples+1):
        for num in range (1, nTables+1):
            print('{0:>2}'.format(num),'*','{0:>2}'.format(multiples),'=','{0:>3}'.format(num*multiples),'\t', end='')
        print()

def main():
    nTables=int(input('Enter number of multiplication tables: '))
    nMultiples = int(input('Enter number of multiples: '))
    printTable(nMultiples,nTables)

if __name__=='__main__':
    main()

