# OPEN, PROCESS, CLOSE files

# A - create .txt file
todos = open('todos.txt', 'a')

# B - process (edit) file with print()

print('Put out the trash', file=todos)
print('Feed the cat', file=todos)
print('Prepare tax return', file=todos)

# C - close file with .close()
todos.close()

