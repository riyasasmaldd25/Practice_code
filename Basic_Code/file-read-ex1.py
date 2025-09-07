
look_up = input('Please enter the acronmy u are looking for').upper()

with open ('acronyms.txt') as file:
    result = file.readlines()
    found = False
    for line in result:
        if look_up in line:
            print('Here is your result, Happy Learning!!')
            print(line)
            found = True
            break

    if not found:
        print('Sorry the word doesnt exist')