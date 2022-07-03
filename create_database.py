import sqlite3 as sql

# Creates the account tables
# Run this only if you have never ran the server before and
# you have no db file yet
def create_db(con):
    con.execute("""
        CREATE TABLE ACCOUNT (
            rg STRING NOT NULL PRIMARY KEY,
            name TEXT,
            balance DOUBLE);
        """)

# Initializes the connection with the db
def start_db():
    # Creating a database makes the table again
    # Loading one creates the account table anew
    print("Will you start the table anew? (y/n)")

    answer = input()

    # The connection and mysql cursor used for db operations
    con = sql.connect("data.db")
    crsr = con.cursor()

    if answer == 'y':
        # If yes, you'll create the account table
        create_db(con)

    return con, crsr
