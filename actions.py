# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Fatema"
my_age = 23
my_bio = "a smart girl."
myself = Person(my_name, my_bio, my_age)

def introduction():
	print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
	print("Hello %s, Welcome to our portal.\n" % my_name)
	print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")

def options():
    # your code goes here!

    while (True):
    	print("Would you like to:\n")
    	print("1) Create a new club. \n or:\n")
    	print("2) Browse and join club. \n or: \n")
    	print("3) View existing clubs. \n or: \n")
    	print("4) Display members of a club. \n or: \n")
    	print("-1) Close the application. \n")
    	print("^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
    	user_input = input()
    	if (user_input == str(1)):
    		create_club()
    	elif (user_input == str(2)):
    		join_clubs()
    	elif (user_input == str(3)):
    		view_clubs()
    	elif (user_input == str(4)):
    		view_club_members()
    	elif (user_input == str(-1)):
    		print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
    		print("\nBye bye .. \n")
    		print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
    		exit()
    	else:
    		print("Invalid opition ... Try again.\n")


def create_club():
    # your code goes here!
    name = input("\nPick a name for your awesome club:\n\n")
    description = input("\nWhat is your club  about? \n\n")
    new_club = Club(name, description)
    clubs.append(new_club)
    new_club.assign_president(myself)

    print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
    print("Enter the numbers of people you would like to recruit to your new club: \n ")
    i = 0
    for member in population:
    	i = i + 1
    	print("[" + str(i) + "] " + member.name)

    print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
    

    user_pick_num = input()
    while (user_pick_num != str(-1)):
    	mem_location = population[int(user_pick_num) - 1]
    	new_club.recruit_member(mem_location)
    	user_pick_num = input()    	

    else:
    	print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
    	print("Here's your club: \n")
    	print(new_club.name)
    	print()
    	print(new_club.description)
    	print()
    	print("members: \n")
    	print()  
    	
    	new_club.print_member_list()
    

def view_clubs():
    # your code goes here!
    count = 0
    for club in clubs:
    	print("Name: %s" % club.name)
    	print("Description: %s" % club.description)
    	
    	for member in club.group:
    		count = count + 1
    	print("Members: %s" % count)
    	print()
    	count = 0
    print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
    
     


def view_club_members():
    # your code goes here!
    view_clubs()
    pick_club = input("Enter the name of the club that you would like to see its members:\n\n")
    for club in clubs:
    	if pick_club.lower() == club.name.lower():
    		club.print_member_list()

def join_clubs():
    # your code goes here!
    view_clubs()
    pick_club = input("Enter the name of the club that you would like to join: \n\n")

    for club in clubs:
    	if pick_club.lower() == club.name.lower():
    		club.recruit_member(myself)
    		print()
    		print(my_name + " just joined " + club.name)
    		print("\n^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*\n")
    


    
def application():
    introduction()
    # your code goes here!
    options()
    
