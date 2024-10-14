import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True

}

def show_films (cursor,title):
   #Method to execute an inner join on all tables,
   #iterate over the dataset and output the results to the terminal window

   #Inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' "
                   "FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id ORDER BY film.film_id")
    
    #Get the results from the cursor object
    films = cursor.fetchall()
    print("\n -- {} --".format(title))
    
    #iterate over the film dataset and display the results
    for films in films:
        print("Film Name: {}\n Director: {}\n Genre Name ID: {}\n Studio Name: {}\n".format(directors[0],directors[1],directors[2],directors[3]))
    


try:
    db =mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on {} with database {}".format(config["user"], config["host"], config["database"]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    cursor = db.cursor()
    #Display initial films
    show_films(cursor, " DISPLAYING FILMS")

    #Insert a new record into the film table
    #Displaying film after insert
    cursor.execute("INSERT INTO film  VALUES (4,'Jaws','1975','155',' Ridley Scott',3,3)")
    show_films(cursor," DISPLAYING FILMS AFTER INSERT")
    
   
       
    #Displaying films after update 
    #Changed Alien genre from SciFi to Horror
    cursor.execute("UPDATE film SET genre_id = 3 WHERE film_name = 'Alien'")
    show_films(cursor," DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror " )


    #Displaying films after delete
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    show_films(cursor," DISPLAYING FILMS AFTER DELETE ")
     
    db.close()