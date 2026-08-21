print("Welcome to the Password Manager!")
pwd = input("Please enter your master password: ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f:
            data = line.rstrip()
            user, password = data.split("|")
            print(f"Account: {user} | Password: {password}")
            

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to store a new password or retrieve an existing one? (store/retrieve) also enter q to quit: ").lower()
    if mode == "q":
        break
    if mode == "store":
        add()
    elif mode == "retrieve":
        view()
    else:
        print("Invalid mode.")



