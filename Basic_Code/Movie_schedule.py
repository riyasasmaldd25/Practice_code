
current_movies = {'puspa': '11:00am',
                  'Titanic': '1:00pm',
                  'Don': '3:00pm',
                  'Frozen': '5:00pm'}

print("We are showing the following movies:")

for i in current_movies:
    print(i)

movie = input("what movie u wnat the show time for?\n")

if movie in current_movies:
    showtime = current_movies.get(movie)
    print(showtime)

else:
    print(movie + ' is not playing')


#List in dictionary

numbs = {'First': [1,2,3],
          'Second': [4,5,6],
          'Third': [7,8,9]}

for position, lists in numbs.items():
    print(position, ' : ', lists)

    
