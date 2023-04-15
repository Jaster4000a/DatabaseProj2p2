import sqlite3
import traceback

def return_checked_out_borrowers_6():
    # connecting to the database
    connection = sqlite3.connect("LMS.db")

    # cursor
    crsr = connection.cursor()

    # Create the tables if not already created
    crsr.execute(f"""
    SELECT name
    FROM borrower, book_loans
    WHERE date('now')<book_loans.due_date AND book_loans.card_no==borrower.card_no;
    """)

    # crsr.execute("""SELECT MAX("index") FROM book;""")

    # Execute the SELECT query and retrieve the results
    results = crsr.fetchall()
    for result in results:
        print(result)

    connection.close()
    return results

return_checked_out_borrowers_6()