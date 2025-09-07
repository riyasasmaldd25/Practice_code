
contacts = {
    'number': 5,
    'students': 
        [
            {'name': 'riya', 'email': 'rsasmal@akamai.com'},
            {'name': 'pooja', 'email': 'pooja@akamai.com'},
            {'name': 'sam', 'email': 'sma@akamai.com'},
            {'name': 'rik', 'email': 'rik@akamai.com'},
            {'name': 'tom', 'email': 'tom@akamai.com'}
        ]
}

print('students emails:')

for student in contacts['students']:
    print(student['email'])

