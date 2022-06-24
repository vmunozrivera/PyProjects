# Manage Files
# Create, read and write a file

file = open('new_file.txt', 'w')
file.write('New file created!\n')
file.close()

file = open('new_file.txt', 'r+')
file.readline()
file.write('New file modification log\n')

file.seek(0)
print(file.read())
file.close()
