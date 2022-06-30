Create: c <RG number> <name>
    > OK
    > ERROR: Repeated RG
Update: u <RG number> <new name>
    > OK
    > ERROR: RG is not registered
Delete: r <RG number>
    > OK
    > ERROR: RG is not registered

Consult balance: b <RG number>
    > BALANCE: <balance>
    > ERROR: RG is not registered

Withdraw: w <RG number> <value>
    > OK
    > ERROR: RG is not registered
    > ERROR: Insufficient funds
Deposit: d <RG number> <value>
    > OK
    > ERROR: RG is not registered

Transfer: t <sender RG no> <receiver RG no> <value>
    > OK
    > ERROR: Sender RG is not registered
    > ERROR: Receiver RG is not registered
    > ERROR: Insufficient funds
