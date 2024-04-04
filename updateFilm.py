from connect import *

def update_film_record():
    try:
        dbCon, dbCursor = db_access()

        filmID = int(input("Enter the filmID of the film to update: "))
        dbCursor.execute("SELECT * FROM tblFilms Where filmID = ?", (filmID,))

        row = dbCursor.fetchone()
        if row == None:
            print(f"No record with the filmID {filmID} exists.")
       
        else:
            num_fields = input("Enter N to update one field ot Y to update all fields: ").upper()

            if num_fields == "Y":
                film_title = input("Enter new film title: ")
                film_yearReleased = input("Enter release year of the film: ")
                film_rating = input("Enter film rating: ")
                film_duration = input("Enter film duration: ")
                film_genre = input("Enter film genre: ")

                dbCursor.execute(f"UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ? ", (film_title, film_yearReleased, film_rating, film_duration, film_genre, filmID,))
                dbCon.commit()
                print(f"Record {filmID} updated!")
            elif num_fields == "N":
                field_name = input("Enter the field (title, yearReleased, rating, duration or genre): ")
                if field_name not in ["title", "yearReleased", "rating", "duration", "genre"]:    
                    print(f"Field {field_name} not a field name in the table!")
                else:
                    field_value = input(f"Enter the value for the field {field_name}: ")
                    dbCursor.execute(f"UPDATE tblFilms SET {field_name} = ? WHERE filmID = ?", (field_value, filmID, ))
                    dbCon.commit()
                    print(f"Record {filmID} updated")
            else:
                print(f"Invalied entry! ")
    except sql.ProgrammingError as e:
        print(f"Update error: {e}")

if __name__ == "__main__":
    update_film_record()       
    



   