import sqlite3
import traceback

def return_borrower_address_from_book_10(title):
    # connecting to the database
    connection = sqlite3.connect("LMS.db")

    # cursor
    crsr = connection.cursor()

    # Create the tables if not already created
    crsr.execute(f"""SELECT name, address
        FROM borrower, book_loans, book
        WHERE book.title="{title}" AND book.book_id==book_loans.book_id AND book_loans.card_no==borrower.card_no""")

    # Execute the SELECT query and retrieve the results
    results = crsr.fetchall()
    for result in results:
        print(result)

    connection.close()
    return results

return_borrower_address_from_book_10("The Great Gatsby")