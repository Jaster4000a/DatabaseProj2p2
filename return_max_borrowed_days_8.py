import sqlite3
import traceback

def return_max_borrowed_days_8():
    # connecting to the database
    connection = sqlite3.connect("LMS.db")

    # cursor
    crsr = connection.cursor()

    # Create the tables if not already created
    crsr.execute("""SELECT MAX(julianday(Returned_date)-julianday(date_out))
                FROM book_loans;""")

    # Execute the SELECT query and retrieve the results
    results = crsr.fetchall()
    for result in results:
        print(result)

    connection.close()
    return results

return_max_borrowed_days_8()