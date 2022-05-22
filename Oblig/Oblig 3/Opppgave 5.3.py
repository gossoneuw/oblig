movies = [
    {'title': 'inception', 'year': 2010, 'rating': 8.7},
    {'title': 'inside out', 'year': 2015, 'rating': 8.1},
    {'title': 'con air', 'year': 1997, 'rating': 6.9}
]


def add_movie(list, name, year, rating=5.0):
    list.append({'title': name, 'year': year, 'rating': rating})



add_movie(movies, 'no time to die', 2021, 9.1)
add_movie(movies, 'the boss baby', 2017, 8.1)
add_movie(movies, 'dune', 2021, 3.9)
add_movie(movies, 'spiral', 2021,)

print(movies)


def print_movies():
    for movie in movies:
        print(f"\n{movie['title']}-{movie['year']} has a rating of {movie['rating']}")


print_movies()


def avarage_rating():
    ratings = []
    for movie in movies:
        ratings.append(movie['rating'])
    return (round(sum(ratings)/len(ratings),1))


print(f"\n==============================")
print(f"\nthe avarage rating for these movies is {avarage_rating()}")
print(f"\n==============================")

#vi kan bruke funksjonen print_movies til hjelp når vi skal lage en liste som printer ut alle filmer etter et gitt år.


def print_movie_after_year(list, year):
    for movie in list:
        if movie['year'] >= year:
            print(f"\n{movie['title']}-{movie['year']} has a rating of {movie['rating']}")


print_movie_after_year(movies, 2010)



def list_to_txt(movie_list, filename):
    with open (f"{filename}", "w") as file:
        for element in movie_list:
            file.write(str(element))


list_to_txt(movies, "movie_titles.txt")
