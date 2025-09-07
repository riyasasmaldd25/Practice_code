

acronym = input('Enter the acronym u want to add to the file\n').upper()
defination = input('Enter the defination of your acronym\n')

with open('acronyms.txt','a') as file:
    file.write(acronym + ' - '+ defination + '\n')

#print("Your acronym was added successfully!")
