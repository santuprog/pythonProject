vowels='aeiou'
vowelcount=0
for ch in vowels:
    print(ch)
    vowelcount+='encyclopedia'.count(ch)
print(vowelcount)

colours='green, red, blue,red,red,green'
#find
print(colours.find('red'))
#rfind
print(colours.rfind('red'))
#capitalize
print('python IS a Language'.capitalize())
#title
print('Python is a PROGRAMMING Language'.title())
#lower
print('SanTu@gmAiL.com'.lower())
#upper
print('santu@gmaiL.com'.upper())
#swapcase
print('Python is a PROGRAMMING Language'.swapcase())
#islower
print('santu@gmail.com'.islower())
#isupper
print('santu@gmail.com'.isupper())
#istitle
print('Python Is A Programming Language'.istitle())
print('pYTHON IS A programming lANGUAGE'.istitle())
#replace
message=('Amey my friend, Amey my guide')
print(message.replace('Amey','Vihan'))

