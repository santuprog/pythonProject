def strings():
    message='hello Santu'
    print(len(message))

    print(message[0])

    print(message[9])

    index=len(message)-1
    print(message[index])

    print(message[-3])

    print(message[-1])

    message=''
    print(len(message))

    #message[0]='1'
    print(message)

    message_1='Santu'
    message_2='karmakar'
    message=message_1+message_2
    message=message_1*4+message_2
    print(message)

    print(max(message_1,message_2))
    print(max('AZ', 'C', 'AA', ))
    print(max('AZ', 'C', 'AA', 'CC'))
    print(max('AZ', 'C', 'AA', 'CC', 'BD', 'BT'))
    print(message)
    print(message[0:5])
    print(message[5:10])
    print(message[10:len(message)-1])
    print(message[:len(message)-1])
    hello=''
    for k in message:
        hello=hello+k+' '
    print(hello)

    print(message.count('S'))

    vowels='aeiouAEIOU'
    vowelcount=0
    for k in vowels:
        vowelcount+=message.count(k)
    print(vowelcount)

    colors='Red, Green, Blue, Yellow, Purple'
    print(type(colors))
    x=colors.find('Blue')
    print(x)

    colors = 'Red, Green, Blue, Yellow, Purple, Blue'
    y = colors.rfind('Blue')
    print(y)

    print('python is a language'.capitalize())
    print('python is a language'.title())
    print('python is a language'.upper())
    print('python is a language'.title().swapcase())
    print('python is a language'.islower())
    print('python is a language'.upper().isupper())
    print('python is a language'.title().istitle())

    message='python is a language'
    print(message.replace('python','Java'))

    print('    hello how are you    '.lstrip())
    print('    hello how are you    '.rstrip())
    print('    hello how are you    '.strip())

    print(colors.split(','))
    print(colors.split())
    print('hello! how are you'.partition('!'))

    print('>'.join(['I', 'am', 'ok']))
    print(' '.join(['I', 'am', 'ok']))

    name='Albert Einstein'
    print(name.isalpha())
    y='2024'
    print(y.isdigit())
    z='          \n\t'
    print(z.isspace())


    password=input('Enter the password:')
    print(password.isalnum())

    name='Santu Karmakar'
    print(name.endswith('Karmakar'))
    print(name.startswith('Santu'))

    strl='message'.encode('utf16')
    print(strl)
    print(strl.decode('utf16'))

def main():
    strings()

if __name__=='__main__':
    main()
