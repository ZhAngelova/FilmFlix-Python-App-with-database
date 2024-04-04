from connect import *

def insert_record():
    try:
        dbCon, dbCursor = db_access()

        # create a variabe for each field
        film_title = input("Enter film title: ").capitalize()
        film_yearReleased = input("Enter release year of the film: ")
        film_rating = input("Enter film rating: ").title()
        film_duration = input("Enter film duration: ")
        film_genre = input("Enter film genre: ").capitalize()

        dbCursor.execute("INSERT INTO tblFilms VALUES(NULL, ?, ?, ?, ?, ?)", (film_title, film_yearReleased, film_rating, film_duration, film_genre))
        #permanently write the record/data to the table in the database:
        dbCon.commit() 
        print(f"{film_title} insert in the film table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")

    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")

    except sql.Error as er:
        print(f"This error: {er}")    

if __name__ == "__main__":
    insert_record()        