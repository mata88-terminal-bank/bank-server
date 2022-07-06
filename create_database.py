import sqlite3 as sql

# Creates the account tables
# Run this only if you have never ran the server before and
# you have no db file yet
def create_db(crsr):
    crsr.execute("""
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
    con = sql.connect("data.db", check_same_thread=False)
    crsr = con.cursor()

    if answer == 'y':
        # If yes, you'll create the account table
        create_db(crsr)

    return con, crsr

def connect_db_new_thread():
    con = sql.connect("data.db")
    crsr = con.cursor()
    return con, crsr
