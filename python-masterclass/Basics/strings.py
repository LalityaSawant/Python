print('Python strings are easy to use')
print('we can use "" in these quotes')
print("we can use '' in these quotes")
print('hello ' + 'world')

greeting = 'hello'
name = 'someone'

print( greeting + ' ' + name)

#name = input('Please enter your name: ')

print(greeting + ' ' + name)

print('trying \t here \n also print new line')

print('''i can typ eher any'thing as i am doing " now''')

splitstring = '''this string has 
been splited 
over several 
lines'''

print(splitstring)

splitstring = '''this string has \
been splited \
over several \
lines'''

print(splitstring)

print('C:\\users\\test\\notebook\something')
print(r'C:\users\test\notebook\something')

parrot = 'Green parrot'
print(parrot[0:4])
print(parrot[4:8])
print(parrot[0:])
print(parrot[:7])

print(parrot[1:])

print(parrot[-1:-2])

alphabets = 'abcdefghijklmnopqrstuvwxyz'

print(alphabets[::4])

print("string 1 " + "String 2")
print('hello '* 5)

age = 24
print('My age is ' +str(age) + ' years')
print('My age is {0} years'.format(age))
print(f'My age is {age} years')

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31,'Jan','Mar','May','Jul','Aug','Oct','Dec'))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {1}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28,30,31))

for i in range(1,11):
    print('{0} square is {1} and cube is {2}'.format(i,i**2,i**3))

print('right aligned')
for i in range(1,11):
    print('{0:2} square is {1:3} and cube is {2:4}'.format(i,i**2,i**3))

print('left aligned')

for i in range(1,11):
    print('{0:<2} square is {1:<3} and cube is {2:<4}'.format(i,i**2,i**3))

print('left/right/center aligned')

for i in range(1,11):
    print('{0:>2} square is {1:<3} and cube is {2:^4}'.format(i,i**2,i**3))

print(f'Pi is approximately {(22/7):12.50f}')
