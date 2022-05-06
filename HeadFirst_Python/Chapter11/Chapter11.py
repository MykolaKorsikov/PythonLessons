# Exception handling
import sys

print('Example 1: File not found error:')
try:
    with open('myfiles.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('This is not allowed')
except:
    print('Some other error occurred.')

print('\nExample 2: Division by zero:')
try:
    a = 1 / 0
except:
    err = sys.exc_info()
    for e in err:
        print(e)
