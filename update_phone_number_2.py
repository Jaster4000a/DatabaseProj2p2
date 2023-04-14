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
    UPDATE BORROWER
    SET phone=837-721-8965
"""
manual_command(command)