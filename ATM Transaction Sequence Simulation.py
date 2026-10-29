balance=5000
while True:
        print("1.Withdraw 2.Deposit 3.Bal 4.Exit")
        ch=int(input("Choice: "))
        if ch==1:
           amt=int(input("Amount: "))
           if amt<=balance:
                balance=balance-amt
                print(f"New Balance {balance}")
                print()
           else:
                print("Insufficient Balance")
                print()
        elif ch==2:
            amt=int(input("Amount: "))
            balance=balance+amt
            print(f"Balance {balance}")
            print()
        elif ch==3:
             print(f"Balance {balance}")
             print()
        else:
             print("Exit")
             break
