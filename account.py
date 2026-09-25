import random
from data import account_records


def create_account():
    print("\n--- REGISTRATION ---")


    usr = input("Enter your full name: ").strip()
    while len(usr) == 0:
        print("Field cannot be empty!")
        usr = input("Enter your full name: ").strip()


    mob = input("Enter 10-digit mobile number: ").strip()
    while not (mob.isdigit() and len(mob) == 10):
        print("Mobile number must contain exactly 10 digits.")
        mob = input("Enter 10-digit mobile number: ").strip()

    passcode = input("Set a 4-digit PIN: ").strip()
    while not (passcode.isdigit() and len(passcode) == 4):
        print("PIN must be 4 digits!")
        passcode = input("Set a 4-digit PIN: ").strip()

    acc_id = str(random.randint(100000, 999999))
    while acc_id in account_records:
        acc_id = str(random.randint(100000, 999999))

    account_records[acc_id] = {
        'name': usr,
        'phone': mob,
        'pin': passcode,
        'balance': 0.0,
        'history': []
    }

    print("\nAccount setup complete.")
    print("Your Account ID is:", acc_id)
    return acc_id