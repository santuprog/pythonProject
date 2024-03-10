def authenticateUser(password):
    '''
    to authenticate an user and allow access to system
    input parameters: password- string
    return value : message - string
    '''
    if password == 'magic':
        message = ' Login Successful !! \n Welcome to system.'
    else:
        message='password mismatch !!\n'
    return message

def main():
    '''
    to authinticate user
    input parameters: none
    return value: none
    '''
    print('\t LOGIN SYSTEM')
    print('++++++++++++++++++++++++++++++++++++++++++')
    password = input('Enter Password: ')
    message =authenticateUser(password)
    print(message)

if __name__=="__main__":
    main()

