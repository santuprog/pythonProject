def discount(price):
    '''
    Objective: to compute discount
    Input: Price --numeric
    Return : None
    '''

    pass

def sellingPrice(price):
    '''
    Objective: to compute selling price
    Input: Price --numeric
    Return : selling price
    '''
    discountedPrice=discount(price)
    if discountedPrice == None:
        return price
    else:
        return discountedPrice

def main():
    '''
    Objective: to compute discount
    Input:none
    Return : None
    '''
    price=float(input('Enter price:'))
    print('selling price is', sellingPrice(price))

if __name__=='__main__':
    main()