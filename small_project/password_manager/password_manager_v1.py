import json
import sys
import os
FILE = "data.json"

def load_file():
    if not os.path.exists(FILE):
        return {}
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:   # catches empty or corrupted file
        return {}

def save_file(python_obj):
	with open(FILE, "w") as f:
		json.dump(python_obj, f, indent = 2)

def add_data(account, username, password):
	python_obj = load_file()
	python_obj[account] ={"username" : username , "password" :password}  # add new entry or update existing entry in python dict
	save_file(python_obj)

def view_data(account):
	x = load_file()
	return x.get(account)







while True:
	print("Welcome to Password genrator! ")
	option = input("Type A to store password  R for retrieve the password and Q to quit: ").lower()
	if option == "q":
		sys.exit()
		
	if option == "a":
		account = input("Enter account: ")
		username = input("Enter username: ")
		password = input("Enter password: ")
		add_data(account, username,password)
		print("data saved ")
	elif option == "r":
		account = input("Enter username: ")
		result = view_data(account)
		if result is None:
			print("Account not found!")
		else:
			print(f"{account} : {result}")
	else:
		print(" Please type correct option")
			
			