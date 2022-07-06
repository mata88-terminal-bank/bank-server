from account_operations import (
        create_account,
        update_account,
        delete_account,
        consult_account_balance,
        withdraw_from_account,
        deposit_into_account,
        transfer_between_accounts)
from datetime import datetime
from shared import busylist, stamp_time
from time import sleep


# This is simply a parser that will get the raw request string and redirect you
# to the proper operation, then get its return data and return it
def process_request(request, con, crsr):
    # The global busylist holds, for every thread, all of the busy bank accounts
    # by their respective RG numbers
    global busylist

    # This is the Lamport time global variable
    global stamp_time

    # We will break down the string to handle the processes 
    split_request = request.split()

    # Commands without at least the rg number parameter are bad commands
    if len(split_request) > 1:
        # The first part is the command itself
        command = split_request[0]
        # The rg number of the accountholder
        rg_no = split_request[1]

        print("DEBUG", busylist)

        # Test if we are busy
        # We create a flag to check if the current RG is busy
        is_busy = True

        # While the RG is indeed busy, we keep looping and checking again if we
        # are finally free to run
        while is_busy:
            is_busy = rg_no in busylist
            if is_busy:
                print("Got blocked")
                sleep(1)

        # If we reach this point, it means the RG was free

        # Updates lamport timing
        stamp_time = stamp_time + 1
        cur_date = datetime.now()

        # These will be returned by some operation
        status = None
        msg = None

        # Demuxing by bank operation command, and passing its arguments
        if command.lower() == 'c': 
            # 3 arguments minimum
            if len(split_request) < 3:
                return str(f"ERROR: Invalid input: missing arguments")
            name = split_request[2]

            # The RG goes to the busylist now
            busylist.append(rg_no)
            sleep(10)
            print("Locking", rg_no)

            status, msg = create_account(con, crsr, rg_no, name)
        elif command.lower() == 'u': 
            # 3 arguments minimum
            if len(split_request) < 3:
                return str(f"ERROR: Invalid input: missing arguments")
            name = split_request[2]

            # You can only get here once your RG is not busy
            busylist.append(rg_no)
            sleep(10)
            print("Locking", rg_no)

            status, msg = update_account(con, crsr, rg_no, name)
        elif command.lower() == 'r': 
            # 2 arguments minimum
            if len(split_request) < 2:
                return str(f"ERROR: Invalid input: missing arguments")

            # You can only get here once your RG is not busy
            busylist.append(rg_no)
            sleep(10)
            print("Locking", rg_no)

            status, msg = delete_account(con, crsr, rg_no)
        elif command.lower() == 'b': 
            # 2 arguments minimum
            if len(split_request) < 2:
                return str(f"ERROR: Invalid input: missing arguments")

            # You can only get here once your RG is not busy
            busylist.append(rg_no)
            sleep(10)
            print("Locking", rg_no)

            status, msg = consult_account_balance(con, crsr, rg_no)
        elif command.lower() == 'w': 
            # 3 arguments minimum
            if len(split_request) < 3:
                return str(f"ERROR: Invalid input: missing arguments")
            value = split_request[2]

            # You can only get here once your RG is not busy
            busylist.append(rg_no)
            sleep(10)
            print("Locking", rg_no)

            status, msg = withdraw_from_account(con, crsr, rg_no, value)
        elif command.lower() == 'd': 
            # 3 arguments minimum
            if len(split_request) < 3:
                return str(f"ERROR: Invalid input: missing arguments")
            value = split_request[2]

            # You can only get here once your RG is not busy
            busylist.append(rg_no)
            sleep(10)
            print("Locking", rg_no)

            status, msg = deposit_into_account(con, crsr, rg_no, value)
        elif command.lower() == 't': 
            # 4 arguments minimum
            if len(split_request) < 4:
                return str(f"ERROR: Invalid input: missing arguments")
            receiver_rg_no = split_request[2]
            value = split_request[3]

            # You can only get here once your RG is not busy
            busylist.append(rg_no)
            sleep(10)
            print("Locking", rg_no)

            status, msg = transfer_between_accounts(con, crsr, rg_no, receiver_rg_no, value)
        else:
            # Bad command name given
            return str(f"ERROR: Invalid input")

        # Set the RG as free
        print("DEBUG 2", busylist)
        busylist.remove(rg_no)

        # Adds lamport time to the returned message
        msg = msg + '\n (LAMPORT_TIME={}, LOCAL_TIME={})'.format(stamp_time, cur_date)
        print('BANK_ACCOUNT={}: LAMPORT_TIME={}, LOCAL_TIME={}'.format(rg_no, stamp_time, cur_date))

        if status:
            return str(msg)
        # Operations that returned false have failed, thus the error
        else: 
            return str(f"ERROR: {msg}")

    # Account RG argument was not given
    else:
        return str(f"ERROR: Invalid input: missing account identification")
