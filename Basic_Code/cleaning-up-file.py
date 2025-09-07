
import os

original_f = '/Users/rsasmal/python-practice'
destination_f = '/Users/rsasmal/python-practice/CleanUp'

#create a new directory- CleanUp
os.mkdir(destination_f)

# Move the files:
for entry in os.scandir(original_f):
    location_o = os.path.join(original_f, entry.name)
    location_d = os.path.join(destination_f, entry.name)

    if os.path.isfile(location_o):
        os.rename(location_o,location_d)



def check_up():
    for entry in os.scandir(original_f):
        if os.path.isfile(entry):
            print('File: ', entry.name)

        elif os.path.isdir(entry):
            print('Directory: ', entry.name)