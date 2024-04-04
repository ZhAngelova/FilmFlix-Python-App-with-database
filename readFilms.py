from connect import *


def read_films():
    try:
        dbCon, dbCursor = db_access()
        
        # invoke the cursor.execute method to select all the records from the table
        dbCursor.execute("SELECT * FROM tblFilms")
        #fetch all selected records using the fetchall method and assigned it to a variable
        all_films = dbCursor.fetchall()

        if all_films:
        # display a line of 100 * from left to right
            print("*" * 100)   
            # format the heading using field name: filmID, title, yearReleased, rating, duration, genre 
            print(f"filmID{'':<4}|title{'':<30}|yearReleased{'':<2}|rating{'':<2}|duration{'':<2}|genre{'':<10}")
            print("*" * 100)
            for aRecord in all_films:
                print(f"{aRecord[0]:<10}|{aRecord[1]:<35}|{aRecord[2]:<14}|{aRecord[3]:<8}|{aRecord[4]:<10}|{aRecord[5]:<15}")
                print("-" * 100)
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
if __name__ == "__main__":
    read_films()       
        
            