from datetime import datetime
from data import account_records


def deposit(acc_id):
    val = input("Enter deposit amount: ").strip()

    try:
        amt = float(val)
        if amt <= 0:
            print("Amount must be higher than 0.")
            return
    except ValueError:
        print("Input is not a valid numerical amount.")
        return

    account_records[acc_id]['balance'] += amt

    dt_stamp = datetime.now().strftime("%Y/%m/%d %H:%M")
    account_records[acc_id]['history'].append(f"[{dt_stamp}] Credit: +₹{amt:.2f}")

    print(f"Added ₹{amt:.2f} to account.")
    print(f"Current Balance: ₹{account_records[acc_id]['balance']:.2f}")


def withdraw(acc_id):
    val = input("Enter withdrawal amount: ").strip()

    try:
        amt = float(val)
        if amt <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Non-numeric input detected.")
        return

    # balance check
    if account_records[acc_id]['balance'] < amt:
        print("Error: Account has insufficient funds.")
        return

    account_records[acc_id]['balance'] -= amt
    dt_stamp = datetime.now().strftime("%Y/%m/%d %H:%M")
    account_records[acc_id]['history'].append(f"[{dt_stamp}] Debit: -₹{amt:.2f}")

    print(f"Successfully withdrew ₹{amt:.2f}.")
    print(f"Remaining Balance: ₹{account_records[acc_id]['balance']:.2f}")


def transfer(acc_id):
    target = input("Enter recipient Account ID: ").strip()

    if target not in account_records:
        print("Recipient ID not found.")
        return

    if target == acc_id:
        print("Self-transfers are not allowed.")
        return

    val = input("Enter amount to send: ").strip()
    try:
        amt = float(val)
        if amt <= 0:
            print("Invalid amount.")
            return
    except ValueError:
        print("Please enter digits only.")
        return

    if account_records[acc_id]['balance'] < amt:
        print("Transfer failed: Insufficient balance.")
        return


    account_records[acc_id]['balance'] -= amt
    account_records[target]['balance'] += amt

    dt_stamp = datetime.now().strftime("%Y/%m/%d %H:%M")

    account_records[acc_id]['history'].append(f"[{dt_stamp}] Sent ₹{amt:.2f} to ID {target}")
    account_records[target]['history'].append(f"[{dt_stamp}] Recv ₹{amt:.2f} from ID {acc_id}")

    print("Funds transferred successfully!")


def show_balance(acc_id):
    print(f"\nAccount Balance: ₹{account_records[acc_id]['balance']:.2f}")


def transaction_history(acc_id):
    logs = account_records[acc_id]['history']

    print("\n--- STATEMENT ---")
    if not logs:
        print("No transactions on record.")
    else:
        for idx, entry in enumerate(logs, start=1):
            print(f"{idx}. {entry}")
    print("-----------------")