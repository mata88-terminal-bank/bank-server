# Db operations per se
# Remember to pass the connection and cursor to connnect to the db

# Creates a new row into the account table
# The balance always starts at 0, make a deposit/transfer to add funds
def create_entry(con, crsr, rg_no, name):
    sql = f"INSERT INTO ACCOUNT VALUES ({rg_no}, '{name}', 0)"
    crsr.execute(sql)
    con.commit()

# Queries the account table filtering by rg number, and gets the passed fields
# The fields must be named exactly as in the mysql table (rg, name, balance)
def read_entry(con, crsr, rg_no, field):
    sql = f"SELECT {field} FROM ACCOUNT WHERE rg = {rg_no}"
    # Returns a list of rows
    crsr.execute(sql)
    return crsr.fetchall()

# Updates account table rows with a matching rg number
# Pass a field to be edited and its new value
# It can only alter one field at a time
# If the value to add to a field is a string, 
# then pass it with 'quotes' in it, such as f"'value'"
def update_entry(con, crsr, rg_no, field, field_data):
    print("Field is", field)
    print("Fielddata is", field_data)
    sql = f"UPDATE ACCOUNT SET {field} = {field_data} WHERE rg = {rg_no}"
    crsr.execute(sql)
    con.commit()

# Removes a row from the account table with a matching rg number
def delete_entry(con, crsr, rg_no):
    sql = f"DELETE FROM ACCOUNT WHERE rg = {rg_no}"
    crsr.execute(sql)
    con.commit()
