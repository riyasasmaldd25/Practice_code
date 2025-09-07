import os

# Make a directory
#os.mkdir('/Users/rsasmal/python-practice/code-merge_')

#list the files of a directory

folder = '/Users/rsasmal/python-practice'
destination = '/Users/rsasmal/python-practice/code-merge_'
entries = os.scandir(folder)
for entry in entries:
    if os.path.isfile(entry):
        print('File:',entry.name)

    elif os.path.isdir(entry):
        print('Dir:', entry.name)

new_file_add = os.path.join(destination, 'new-file')

with open(new_file_add, 'w') as file:
    file.write("Hellow!! i created a new file")


