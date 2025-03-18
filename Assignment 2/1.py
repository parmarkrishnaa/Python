# WAP to take users favourtie movies and store it in a list and print it at the end

name = int(input("Enter your favourite movies: "))

movie = []

i = 1

while i <= name:
    movie_name = input("Enter your favourite movies: ")
    movie.append(movie_name)
    i += 1
    
print(movie)