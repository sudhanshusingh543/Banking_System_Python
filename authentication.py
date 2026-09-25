from data import account_records

def login():
    print("\n--- LOGIN SECTION ---")
    acc_id = input("Account ID: ").strip()
    passcode = input("PIN: ").strip()


    if acc_id not in account_records:
        print("No matching account found.")
        return None

    if account_records[acc_id]['pin'] != passcode:
        print("Invalid PIN.")
        return None

    print(f"\nWelcome back, {account_records[acc_id]['name']}!")
    return acc_id


def change_pin(acc_id):
    current = input("Enter current PIN: ").strip()

    if account_records[acc_id]['pin'] != current:
        print("Wrong current PIN provided.")
        return

    new_pass = input("New 4-digit PIN: ").strip()
    if not (new_pass.isdigit() and len(new_pass) == 4):
        print("New PIN is invalid. Operations cancelled.")
        return

    match_check = input("Re-enter new PIN to confirm: ").strip()
    if new_pass != match_check:
        print("PINs do not match!")
        return

    account_records[acc_id]['pin'] = new_pass
    print("PIN changed successfully.")