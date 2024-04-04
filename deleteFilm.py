from connect import *

def delete_film():
    try:
        dbCon, dbCursor = db_access()

        filmID = int(input("Enter the filmID of the film to delete: "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (filmID,))   
        
    
        row = dbCursor.fetchone()
        
        if row == None:
            print(f"No record with filmID {filmID} in the films table!!")
        else: 
            dbCursor.execute("DELETE FROM tblFilms where filmID = ?", (filmID,))
            dbCon.commit()

            print(f"Record {filmID} deleted from the tblFilms.") 
    except sql.ProgrammingError as e:
        print(f"Delete operation failed: {e}")
if __name__ == "__main__":
    delete_film()                      
    