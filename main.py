from account import create_account
from authentication import login, change_pin
from transactions import (
    deposit,
    withdraw,
    transfer,
    show_balance,
    transaction_history
)


def run_account_session(acc_id):
    active = True
    while active:
        print("\n=== USER DASHBOARD ===")
        print("1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Fund Transfer")
        print("5. Mini Statement")
        print("6. Update PIN")
        print("7. Logout")

        opt = input("Select choice (1-7): ").strip()

        if opt == "1":
            show_balance(acc_id)
        elif opt == "2":
            deposit(acc_id)
        elif opt == "3":
            withdraw(acc_id)
        elif opt == "4":
            transfer(acc_id)
        elif opt == "5":
            transaction_history(acc_id)
        elif opt == "6":
            change_pin(acc_id)
        elif opt == "7":
            print("Logged out.")
            active = False
        else:
            print("Invalid entry, try again.")


def main():
    while True:
        print("\n=== BANKING APP ===")
        print("1. Create Account")
        print("2. Log In")
        print("3. Log Out")

        opt = input("Choice: ").strip()

        if opt == "1":
            create_account()
        elif opt == "2":
            session_id = login()
            if session_id:
                run_account_session(session_id)
        elif opt == "3":
            print("Exiting application...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()