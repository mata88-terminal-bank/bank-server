from account_operations import (
        create_account,
        update_account,
        delete_account,
        consult_account_balance,
        withdraw_from_account,
        deposit_into_account,
        transfer_between_accounts)

# This is simply a parser that will get the raw request string and redirect you
# to the proper operation, then get its return data and return it
def process_request(request, con, crsr):
    # We will break down the string to handle the processes 
    split_request = request.split()

    # Commands without at least the rg number parameter are bad commands
    if len(split_request) > 1:
        # The first part is the command itself
        command = split_request[0]
        # The rg number of the accountholder
        rg_no = split_request[1]
        
        # These will be returned by some operation
        status = None
        msg = None

        # Demuxing by bank operation command, and passing its arguments
        if command == 'c': 
            # 3 arguments minimum
            if len(split_request) < 3:
                return str(f"ERROR: Invalid input: missing arguments")
            name = split_request[2]
            status, msg = create_account(con, crsr, rg_no, name)
        elif command == 'u': 
            # 3 arguments minimum
            if len(split_request) < 3:
                return str(f"ERROR: Invalid input: missing arguments")
            name = split_request[2]
            status, msg = update_account(con, crsr, rg_no, name)
        elif command == 'r': 
            # 2 arguments minimum
            if len(split_request) < 2:
                return str(f"ERROR: Invalid input: missing arguments")
            status, msg = delete_account(con, crsr, rg_no)
        elif command == 'b': 
            # 2 arguments minimum
            if len(split_request) < 2:
                return str(f"ERROR: Invalid input: missing arguments")
            status, msg = consult_account_balance(con, crsr, rg_no)
        elif command == 'w': 
            # 3 arguments minimum
            if len(split_request) < 3:
                return str(f"ERROR: Invalid input: missing arguments")
            value = split_request[2]
            status, msg = withdraw_from_account(con, crsr, rg_no, value)
        elif command == 'd': 
            # 3 arguments minimum
            if len(split_request) < 3:
                return str(f"ERROR: Invalid input: missing arguments")
            value = split_request[2]
            status, msg = deposit_into_account(con, crsr, rg_no, value)
        elif command == 't': 
            # 4 arguments minimum
            if len(split_request) < 4:
                return str(f"ERROR: Invalid input: missing arguments")
            receiver_rg_no = split_request[2]
            value = split_request[3]
            status, msg = transfer_between_accounts(con, crsr, rg_no, receiver_rg_no, value)
        else:
            # Bad command name given
            return str(f"ERROR: Invalid input")

        if status:
            return str(msg)
        # Operations that returned false have failed, thus the error
        else: 
            return str(f"ERROR: {msg}")

    # Account RG argument was not given
    else:
        return str(f"ERROR: Invalid input: missing account identification")
