import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}


conn = mysql.connector.connect(**config)


cursor = conn.cursor()

# First query to select all the fields for studio table.

cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
print("-- DISPLAYING Studio Records --")
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

# Second query to select all the fields for genre table.
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
print("\n-- DISPLAYING Genre Records --")
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

# Third query to select the movie names for those movies that have a run time of less than two hours.
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
short_movies = cursor.fetchall()
print("\n-- DISPLAYING Short Film Records --")
for movie in short_movies:
    print("Film Name: {}\nRuntime: {}".format(movie[0], movie[1]))

# Fourth query to get a list of film names, and directors grouped by director. 
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director, film_name")
films_and_directors = cursor.fetchall()
print("\n-- DISPLAYING Director RECORDS in Order --")
for entry in films_and_directors:
    film, director = entry
    print("Film Name: {}\nDirector: {}\n".format(film, director))

cursor.close()
conn.close()