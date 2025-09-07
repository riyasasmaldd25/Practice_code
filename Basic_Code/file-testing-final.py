
def find_acronym(file_name):
    look_up = input('Please enter the acronmy u are looking for\n').upper()

    try:
        with open (file_name) as file:
            result = file.readlines()
            found = False
            for line in result:
                if look_up in line:
                    print('Here is your result, Happy Learning!!')
                    print(line)
                    found = True
                    break

    except FileNotFoundError as e:
        print('File doesnt exist, try with another file or a new one')

    if not found:
        print('Sorry the word doesnt exist')

def add_acronym(file_name):
    acronym = input('Enter the acronym u want to add to the file\n').upper()
    defination = input('Enter the defination of your acronym\n')

    with open(file_name,'a') as file:
        file.write(acronym + ' - '+ defination + '\n')

    print("Your acronym was added successfully!")

#Main Function:

def main():
    print('we have two sets of file mentioned below:\n')
    print('acronyms.txt - file for Reading\n')
    print('listing.txt - File for adding new acronyms')
    file_name = input('Please enter the file as per your preference from above mentioned list: add/read \n').lower()
    #interest = input('Please let me know whether you wnat to add an acronym or read an acronym? ADD/READ \n').lower()

    if file_name == 'listing.txt':
        add_acronym(file_name)

    else:
        find_acronym(file_name)

main()

