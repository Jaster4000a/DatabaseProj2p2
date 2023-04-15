import sqlite3
import traceback

def insert_book_4a(Title, Author, Publisher):
    # connecting to the database
    connection = sqlite3.connect("LMS.db")

    # cursor
    crsr = connection.cursor()

    # Create the tables if not already created
    crsr.execute(f"""
    INSERT INTO book
    VALUES ((SELECT MAX("index") + 1 FROM book), (SELECT MAX(book_id) + 1 FROM book),"{Title}","{Publisher}");
    """)

    crsr.execute(f"""
    INSERT INTO book_authors
    VALUES ((SELECT MAX("index") + 1 FROM book_authors), (SELECT MAX(book_id) FROM book),"{Author}");
    """)

    # ---Insert logic for inserting a new entry into publisher if they do not already exist on the database ?---



    crsr.execute(f"""
    SELECT *
    FROM book
    """)

    # crsr.execute("""SELECT MAX("index") FROM book;""")

    # Execute the SELECT query and retrieve the results
    results = crsr.fetchall()
    for result in results:
        print(result)

    connection.close()
    return results

insert_book_4a("Harry Potter and the Sorcerer's Stone","J.K. Rowling", "Pottermore Publishing")