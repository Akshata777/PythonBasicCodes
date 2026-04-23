import random
import string

passwords = {}

try:
    with open("password.txt", "r") as file:
        for line in file:
            if ":" in line:
                website, pwd = line.strip().split(":")
                passwords[website] = pwd
except Exception as e:
    print("Error:", e)

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$^&*"
    return "".join(random.choice(chars) for _ in range(8))

while True:
    print("\n---------PASSWORD MANAGER SYSTEM------------")
    print("1. Save Passwords")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("enter your choice: ")

    if choice == "1":
        site = input("enter website: ")
        pwd = input("enter password: ")

        passwords[site] = pwd

        with open("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Saved!")

    elif choice == "2":
        if not passwords:
            print("No data")
        else:
            for site, pwd in passwords.items():
                print(site, ":", pwd)

    elif choice == "3":
        print("Generated Password:", generate_password())

    elif choice == "4":
        print("ok bye...")
        break

    else:
        print("Invalid input")