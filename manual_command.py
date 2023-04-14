import sqlite3

def manual_command(command_string):
    # connecting to the database
    connection = sqlite3.connect("LMS.db")

    # cursor
    crsr = connection.cursor()

    # Create the tables if not already created
    crsr.execute(command_string)
    
    # Execute the SELECT query and retrieve the results
    results = crsr.fetchall()
    for result in results:
        print(result)
    connection.close()
    return results

command="""
    SELECT *
    FROM BORROWER
"""
manual_command(command)