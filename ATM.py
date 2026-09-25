balance=500
pin=1234
entered_pin=int(input("enter pin:"))
if entered_pin!=pin:
    print("wrong pin",)
else:
     print("1.check balance")
     print("2.deposit")
     print("3,withdraw")
     print("4.exit")
choice=int(input("choose option"))
if choice==1:
    print("your balance",balance)
elif choice == 2:
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print(f"Deposited Rs.{amount}. New balance: Rs.{balance}")

elif choice == 3:
    amount = int(input("Enter withdraw amount: "))
    if amount > balance:
        print("Insufficient balance")
    else:
        print(f"Withdrawn Rs.{amount}. New balance: Rs.{balance-amount}")

elif choice == 4:
    print("Thank you. Take your card.")

else:
    print("Invalid choice")

