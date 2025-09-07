
with open ('acronyms.txt') as file:
    result = file.read()
    print(result)
    print('------------------------------------------------------')

    file.seek(0)  # go back to start of file, because read() moved pointer to end
    line_result = file.readlines()
    print('Now we will read the file line by line')
    for line in line_result:
        print(line)
