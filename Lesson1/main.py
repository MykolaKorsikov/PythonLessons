#Option 1
import random

#Option 2
#from random import *

'''
print('Hello World')

print('one', 'two', 'three', sep=', ', end=' ')
print('four')
print(2 + 2)
'''

# comment (type 1)

'''
comments (type 2)
'''

'''
number = 10

name = input('Enter your name: ')

num1 = int(input('Enter first num: '))
num2 = int(input('Enter first num: '))
# num3 = input('Enter first num: ')
result = num1 + num2
print('Sum is: ', num1 + num2)
print('Type: ', type(result))

words = 'Hello \n \t world'
print(words)

words = 'Hello \\n\\ \\t\\ \'world'
print(words)

example3:
name = 'Mykola'
age = 39

# Option1
print('Name: {}\nAge: {}'.format(name, age))
# Option2
print(f'Name: {name}\n Age: {age}')


#importing specific library
#see above

num = random.random()
print(num)

num1 = random.randint(1, 10)
print(num1)



num1 = 10
num2 = 8

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2) #to power of
print(num1 // num2) #whole after devision
print(num1 % num2) #reminder after devision
'''

# number = 10
# number += 2
# number **= 2
# print(number)

print('Exercise 1: \nNothing \nwill work \nunless you do.\n')

print('Exercise 2: \n"Anyone who \n\tstops \n\t\tlearning is old, \n\t\t\twhether at twenty or eighty". \n\t\t\t\t\t\t\t\t Henry Ford')

print('Exercise 3: \n')
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

c = a + b
d = a - b
e = a * b

print('Sum is: ', c)
print('Difference is: ', d)
print('Product is: ', e, '\n')

print('Exercise 4: \n')
first = int(input('Enter first number: '))
second = int(input('Enter second number [%]: '))
d = first * (second / 100)
print('Result is: ', d)

print('\nExercise 5: \n')
height = int(input('Enter height: '))
width = int(input('Enter width: '))
area = height * width
print('Area of rectangular is: ', area)

print('\nExercise 6:')
#Посчитать сумму цифр трехначного числа. Число должно быть рандомным.
threeDigitNumber = random.randint(1, 999)
first = threeDigitNumber // 100
third = threeDigitNumber % 10
#second = threeDigitNumber // 10 % 10
second = threeDigitNumber % 100 // 10
print(threeDigitNumber)
print('\nFirst: ',first,'\nSecond: ',second,'\nThird: ',third)

print('Sum is: ', first+second+third)