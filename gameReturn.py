import feedbackManager as FM
from database import *

def game_return():
    # Handles game return
    # Updates rental file with return date
    game_ID = input("What is the game's ID which is being returned: ")
    return_date = input("Please input the date of return in the format, DD/MM/YYYY: ")

    # Use a temporary list to store updated lines
    updated_lines = []

    with open("Rental.txt", "r") as file:
        # Read all lines into a list
        lines = file.readlines()

    # Flag to check if the game is found in the file
    game_found = False

    # Iterate over the lines to update the return date
    for line in lines:
        if game_ID in line:
            new_line = line.strip().split(",")
            new_line[2] = return_date
            print("Game has been successfully returned and added to the rental history")
            print(new_line)
            string_line = ",".join(new_line)
            updated_lines.append(string_line)
            game_found = True
        else:
            # If the game is not found, add the line unchanged to the updated list
            updated_lines.append(line)

    # If the game is not found, print an error message
    if not game_found:
        print("ERROR: Game not available for return as it does not exist within the system")
        return

    # Write the updated lines back to the file
    with open("Rental.txt", "w") as file:
        file.writelines(updated_lines)
