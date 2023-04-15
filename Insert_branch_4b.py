import sqlite3
import traceback

def insert_branch_4b(Branch_name,Address):
    # connecting to the database
    connection = sqlite3.connect("LMS.db")

    # cursor
    crsr = connection.cursor()

    # Create the tables if not already created
    crsr.execute(f"""
    INSERT INTO library_branch
    VALUES ((SELECT MAX("index") + 1 FROM library_branch), (SELECT MAX(branch_id) + 1 FROM library_branch),"{Branch_name}","{Address}");
    """)

    crsr.execute(f"""
    SELECT *
    FROM library_branch
    """)

    # crsr.execute("""SELECT MAX("index") FROM book;""")

    # Execute the SELECT query and retrieve the results
    results = crsr.fetchall()
    for result in results:
        print(result)

    connection.close()
    return results

insert_branch_4b("North Branch","456 NW, Irving, TX 76100")