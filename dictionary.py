def dictionary_operations():
    '''dictionsy is a unordered sequence of key value pair'''
    month={}
    month[1]='Jan'
    month[2]='Feb'
    month[3]='Mar'
    month[4]='Apr'
    month[5]='May'
    print(month)

    '''vegetable prices'''
    price={'tomato':40,'cucumber':30,'potato':20,'cauliflower':55,'cabbage':60,'carrot':20}
    print(price['potato'])
    print(price['carrot'])
    print(price.keys())
    print(price.values())
    print(price.items())

    '''length'''
    print(len(price))
    '''indexing'''
    print(price['cucumber'])
    '''min works on keys only'''
    print(min(month))
    '''max works on keys only'''
    print(max(month))
    '''sum works on keys only'''
    print(sum(month))
    '''membership'''
    print('tomato' in price)
    '''del to delete'''
    del(price['tomato'])
    print(price)
    '''clear'''
    price.clear()
    print(price)

    '''get function'''
    password={'Ram':'fiohs3123@','Shyam':'sofdi231432#','Gita':'oeirg78954$'}
    print(password.get('Ram',-1))
    print(password.get('Jodu',-1))

    '''update function'''
    morepassword={'Raman':'eeggdfq325#','kishore':'rojngek224*'}
    password.update(morepassword)
    print(password)

    '''copy funtion'''
    newpassword=morepassword.copy()
    print(id(newpassword))
    print(id(morepassword))




def main():
        dictionary_operations()


if __name__ == '__main__':
    main()