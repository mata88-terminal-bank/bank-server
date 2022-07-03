from database import (
        create_entry,
        read_entry,
        update_entry,
        delete_entry)

# This file contains the very bank operations, receiving input parameters
# and returning a message for the user

# Operations return a tuple, a boolean status and a message for the client
# Operations return true in case of success, false in case of failure

# Remember to pass them their connection and cursor to db

def create_account(con, crsr, rg_no, name):
    # Check if account doesn't already exist
    existing_entry = read_entry(con, crsr, rg_no, '*')

    # Each element of the list is a tuple of field values from each found row
    # Hence if the list size is 0, nothing was found
    if len(existing_entry) == 0:
        create_entry(con, crsr, rg_no, name)
        return True, 'OK'
    return False, 'Account already exists'

def update_account(con, crsr, rg_no, name):
    # Check if account exists
    existing_entry = read_entry(con, crsr, rg_no, '*')

    # Each element of the list is a tuple of field values from each found row
    # Hence if the list size is 0, nothing was found
    if len(existing_entry) != 0:
        update_entry(con, crsr, rg_no, 'name', f"'{name}'")
        return True, 'OK'
    return False, 'Account does not exist'

def delete_account(con, crsr, rg_no):
    # Check if account exists
    existing_entry = read_entry(con, crsr, rg_no, '*')

    # Each element of the list is a tuple of field values from each found row
    # Hence if the list size is 0, nothing was found
    if len(existing_entry) != 0:
        delete_entry(con, crsr, rg_no)
        return True, 'OK'
    return False, 'Account does not exist'

def consult_account_balance(con, crsr, rg_no):
    entry = read_entry(con, crsr, rg_no, 'balance, name')

    # Each element of the list is a tuple of field values from each found row
    # Hence if the list size is 0, nothing was found
    if len(entry) != 0:
        # A mysql query here in python returns a list of tuples
        # Each element of the list is a tuple of field values from each found row
        # In each row, its tuple has the fields you've required, in the same order
        balance = entry[0][0]
        account_name = entry[0][1]
        return True, f"Balance for {account_name}: {balance}"
    return False, 'Account does not exist'

def withdraw_from_account(con, crsr, rg_no, value):
    # Check if account exists
    existing_entry = read_entry(con, crsr, rg_no, '*')

    # Each element of the list is a tuple of field values from each found row
    # Hence if the list size is 0, nothing was found
    if len(existing_entry) != 0:
        # Get the current balance
        balance = read_entry(con, crsr, rg_no, 'balance')[0][0]

        # Check if we have enough funds
        if balance >= float(value):
            update_entry(con, crsr, rg_no, 'balance', balance-float(value))
            return True, 'OK'
        return False, 'Insufficient funds'
    return False, 'Account does not exist'

def deposit_into_account(con, crsr, rg_no, value):
    # Check if account exists
    existing_entry = read_entry(con, crsr, rg_no, '*')

    # Each element of the list is a tuple of field values from each found row
    # Hence if the list size is 0, nothing was found
    if len(existing_entry) != 0:
        # Get the current balance
        balance = read_entry(con, crsr, rg_no, 'balance')[0][0]

        update_entry(con, crsr, rg_no, 'balance', balance + float(value))
        return True, 'OK'
    return False, 'Account does not exist'

def transfer_between_accounts(con, crsr, sender_rg_no, receiver_rg_no, value):
    # Check if sender account exists
    sender_entry = read_entry(con, crsr, sender_rg_no, '*')

    # This is a rather complex function, so here is a simplification:
    """
    if (sender account exists)
        if (receiver account exists)
            if (sender has enough funds)
                subtract $value from sender account
                add $value to receiver account
    send status and message
    """

    # Each element of the list is a tuple of field values from each found row
    # Hence if the list size is 0, nothing was found
    if len(sender_entry) != 0:
        # Check if receiver account exists
        receiver_entry = read_entry(con, crsr, receiver_rg_no, '*')

        # Each element of the list is a tuple of field values from each found row
        # Hence if the list size is 0, nothing was found
        if len(receiver_rg_no) != 0:
            # Get the current sender balance
            balance = read_entry(con, crsr, sender_rg_no, 'balance')[0][0]

            # Check if the sender has enough funds
            if balance >= float(value):
                # Withdrawing from sender
                update_entry(con, crsr, sender_rg_no, 'balance', balance-float(value))

                # Deposit into receiver
                # Get the current receiver balance
                balance = read_entry(con, crsr, receiver_rg_no, 'balance')[0][0]

                # Depositing into receiver
                update_entry(con, crsr, receiver_rg_no, 'balance', balance + float(value))
                return True, 'OK'
            return False, 'Insufficient funds'
        return False, 'Receiver account does not exist'
    return False, 'Sender account does not exist'

