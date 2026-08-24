
name = input("Type your name")
print(f"Welcome {name} to this adventure ")

option = input(" You are on dirt road.  Having solo adventure. The road is about to come to an end and you have to choose left for mountain view and right for lake view ").lower()


if option == "left":
	option = input("Welcome to mountain view, you are hiking now. Path is quite rough. You are about to reach 1st camp site. From here take left to hike further. Take right to start descending toward village ")
	if option == "left":
		print("You are now reaching to 2nd camp site and the view from this height is the view is quite beautiful ")
	elif option == "right":
		print(" You are decending now and can see small village with cute rabbits ")
	else:
		print("Sorry, Please type correct option")
elif option == "right":
	option = input("you are reaching toward lake.take left for  bridge and right you can swim ")
	if option == "left":
		print("you are walking on bridge and its wobbling little bit")
	elif option == "right":
		print("you are swimming now and water is quite cold")
	else:
		print("Sorry, Please type correct option")
else:
	print("Sorry, Please type correct option")

	

	
	
	
 

