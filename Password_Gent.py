import random
import string

password={}

try:
    with open("password.txt","r") as f:
        for line in f:
            website,pasw=line.strip().split(":")
            password[website]=pasw
except:
    pass

def generate_password():
    chars=string.ascii_letters + string.digits + "!@#$%^&*()-+"
    password="".join(random.choice(chars) for _ in range(12))
    return password

while True:
    print("\n---Password Manager---")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice=input("Enter your choice :")

    if choice=="1":
        website=input("Enter website :")
        pasw=input("Enter password :")
        password[website]=pasw
        with open("password.txt","w") as f:
            for site,pas in password.items():
                f.write(f"{site}:{pas}\n")

        print("Password saved successfully!")

    elif choice=="2":
        if not password:
            print("No passwords saved yet.")
        else:
            print("\nSaved Passwords:")
            for site,pas in password.items():
               print(f"{site}: {pas}")

    elif choice=="3":
        new_password=generate_password()
        print(f"Generated Password: {new_password}")

    elif choice=="4":
        print("Exiting Password Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    



