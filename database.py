from gameRent import *
from gameReturn import *
from gameSearch import *
from InventoryPruning import *
import subscriptionManager as SM

# gameRent functions
# rent a game
# get_subscription_type()
# rent_game()
# game_availability()
def rent_options():
    # Presents rent options menu and routes user selection 

    keep_going = True
    while keep_going:
        choice = input("Would you like to check the customer's subscription status (S), subscription type (T), the availability of games (A) or (Q) to quit? Please type S, T, A or Q: ")
        if choice == 'S':
            check_subscription_status()
            carry_on = input("Would you like to keep using the system. Type yes or no: ")
            if carry_on == 'no':
                keep_going = False
        elif choice == 'T':
            get_subscription_type()
            carry_on = input("Would you like to keep using the system. Type yes or no: ")
            if carry_on == 'no':
                keep_going = False
        elif choice == 'A':
            game_availability()
            carry_on = input("Would you like to keep using the system. Type yes or no: ")
            if carry_on == 'no':
                keep_going = False
        elif choice == 'Q':
            keep_going = False
        elif choice != 'S' or 'T' or 'A':
            print("ERROR: Input the correct characters")

def rent_game():
# Handles renting a game to a customer
# Gets input, validates, updates rental file
    with open("Game_Info.txt","r+") as f:
        line = f.readline()
        game_ID = input("What game ID would you like to rent?: ")
        CID = input("What is the customer's ID?: ")
        rental_date = input("Please input the date of purchase in the format DD/MM/YYYY: ")
        for line in f:
            if game_ID in line.split(","):
                with open("Rental.txt","r+") as l:
                    fine = l.readline()
                    new_line = fine.strip().split(',')
                    new_line[0] = game_ID
                    new_line[1] = rental_date
                    new_line[2] = "null"
                    new_line[3] = CID
                    string_line =  ','.join(new_line)
                    l.write("\n" + string_line)
                    print(new_line)
                    print(string_line)

def get_subscription_type():
    # Prints customer's subscription type based on input ID

    with open("Subscription_Info.txt","r") as f:
        line = f.readline()           
        CID = input("What is your customer ID?: ")
        ID_counter = 0
        for line in f:
            if CID in line:
                ID_counter += 1
                subscription_type = line[5:12]
                if subscription_type == "Basic,2":
                    sub_type = subscription_type[0:5]
                    print(f"Customer with ID {CID} has a {sub_type} subscription type")
                elif subscription_type == "Premium":               
                    print(f"Customer with ID {CID} has a {subscription_type} subscription type")        
                
        if ID_counter == 0:
            print("ERROR: You do not have a customer ID.")
def check_subscription_status():    
    # Checks if customer ID has active subscription
    # Calls subscriptionManager module
    customer_ID = input("What is the customer's ID?: ")
    sub_status = SM.check_subscription(customer_ID, SM.load_subscriptions())
    if sub_status == True:
        print(f"Customer with ID {customer_ID} has an active subscription")
    else:
        print("ERROR: Subscription status is inactive")


            
def game_availability():
    # Displays availability status for input game IDs
    # Checks if currently rented out
    game_counter = 0
    with open("Rental.txt", "r") as file:
        line = file.readline()
        games = input("Please type the game ID(s) you would like to search for (e.g cod01 fifa02 tlo04): ")
        game_IDs = games.split(',')
        print("Game ID    Rental Date    Return Date    Rented Customer ID")
        
        for line in file:
            for game in game_IDs:
                if game in line:
                    
                    # Split the line into a list of values
                    list_line = line.strip().split(',')
                    
                    # Check if the game has been returned
                    if list_line[2] != "null":
                        game_counter += 1
                        print(list_line)
                    else:
                        # Print an error message if the game has not been returned
                        print(f"ERROR: The game with ID {game} cannot be rented as it has not been returned")
    print(f"There are {game_counter} copies of the game available")

def game_feedback():
    # Logs feedback rating and comments for a game
    # Passes to feedbackManager module
    f = open("Rental.txt","r+")
    line = f.readline() 
    game_ID = input("What is the game's ID?: ")
    rating = input("What would you rate the game on a scale of 0-5?: ")
    comments = input("Do you have any comments about the game?: ")
    FM.add_feedback(game_ID, rating, comments, 'Game_feedback.txt')
    print("Thank you for your feedback!")
    f.close()

# def game_return():
#     # Handles game return 
#     # Updates rental file with return date
#     with open("Rental.txt","r+") as f:
#         line = f.readline() 
#         game_ID = input("What is the game's ID which is being returned: ")
#         return_date = input("Please input the date of return in the format, DD/MM/YYYY: ")
#         for line in f:
#             if game_ID in line:
#                 new_line = line.strip().split(",")
#                 new_line[2] = return_date
#                 print("Game has succesfully been rented and added to rental history")
#                 print(new_line) 
#                 string_line = ','.join(new_line)
#                 f.write('\n')
#                 f.write(string_line)
#             else:
#                 print("ERROR: Game not available for return as it does not exist within the system")

def game_return():
    # Handles game return
    # Updates rental file with return date
    game_ID = input("What is the game's ID which is being returned: ")
    return_date = input("Please input the date of return in the format, DD/MM/YYYY: ")
    CID = input("What is the customer's ID?: ")

    # Use a temporary list to store updated lines
    updated_lines = []

    with open("Rental.txt", "r+") as file:
        # Read all lines into a list
        lines = file.readlines()

    # Flag to check if the game is found in the file
    game_found = False

    # Iterate over the lines to update the return date
    line_list = ""
    for line in lines:
        line_list += line
        if game_ID in line:
            if CID in line:
                new_line = line.strip().split(",")
                new_line[2] = return_date
                print("Game has been successfully returned and added to the rental history")
                print(new_line)
                print(line_list)
                # string_line = ",".join(new_line[2])
                string_line = ",".join(new_line)
                updated_lines.append("\n" + string_line +"\n")
                game_found = True
        else:
            # If the game is not found, add the line unchanged to the updated list
            updated_lines.append(line[2:4])

    # If the game is not found, print an error message
    if not game_found:
        print("ERROR: Game not available for return as it does not exist within the system")
        return

    # Write the updated lines back to the file
    with open("Rental.txt", "w") as file:
        file.write(line_list + "\n")
        file.write(string_line)


def search_game():
    # Searches game catalog based on user criteria 
    # Prints matches to provided search term
    with open("Game_Info.txt","r") as f:
        line = f.readline()
        game_classification = input("Would you like to search for a game's title, genre or platform?: ").lower()
        if game_classification == 'title':
            game_title = input("What is the game's title?: ")
            for line in f:
                if game_title in line:
                    new_line = line.split(",")
                    string_line = ','.join(new_line)
                    print(string_line)                      
        elif game_classification == 'genre':
            game_genre = input("What is the game's genre?: ")
            for line in f:
                if game_genre in line:
                    new_line = line.split(",")
                    string_line = ','.join(new_line)
                    print(string_line)
        elif game_classification == 'platform':
            game_platform = input("What is the game's platform?: ")
            for line in f:
                if game_platform in line:
                    new_line = line.split(",")
                    string_line = ','.join(new_line)
                    print(string_line)

def load_rentals():
    # Analyzes rental data to calculate frequency  
    # For recommending games to remove
    rentals = {}
    with open('Rental.txt') as f:
       
        for line in f:
            data = line.split(',')
            game_id = data[0]
            
           
            if game_id in rentals:
                rentals[game_id] += 1
            else:
                rentals[game_id] = 1
           