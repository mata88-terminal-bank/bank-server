To run the server, run, on this directory:

    python main.py

Once started, this program will prompt you as such:

    "Will you start the table anew? (y/n)"

Answering yes will create a db with a new table.
If there was already a database, then the server will crash.
Simply kill it and answer with a 'n' the next time.
Any answer different from a 'y' counts as a negative response.

Then you can start the client and send one of the following requests.

The RG can actually be any unique string per account without whitespaces.
The name for an accountholder is a string without whitespaces. 
Different accounts can use the same name value.
As for the values, do not use negative numbers.
In case of decimal cases, use '.' dots.

Here are all of the commands and their syntax.

Create: c <RG number> <name>
    > OK
    > ERROR: Account already exists

Update: u <RG number> <new name>
    > OK
    > ERROR: Account does not exist

Delete: r <RG number>
    > OK
    > ERROR: Account does not exist

Consult balance: b <RG number>
    > BALANCE: <balance>
    > ERROR: Account does not exist

Withdraw: w <RG number> <value>
    > OK
    > ERROR: Account does not exist
    > ERROR: Insufficient funds

Deposit: d <RG number> <value>
    > OK
    > ERROR: Account does not exist

Transfer: t <sender RG no> <receiver RG no> <value>
    > OK
    > ERROR: Receiver account does not exist
    > ERROR: Sender account does not exist
    > ERROR: Insufficient funds
