import random as rd

name = input('Enter your name: ')
yob = int(input('Enter your year of birth: '))

year = rd.randint(0,70)
print('Hello', name, 'your lucky year is', (year + yob))