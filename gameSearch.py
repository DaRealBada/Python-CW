import subscriptionManager as SM
from database import *

def search_game():
    # Function to search for a game in the Game_Info.txt file
    with open("Game_Info.txt","r") as f:
        line = f.readline()
        game_classification = input("Would you like to search for a game's title, genre or platform?: ").lower()
        if game_classification == 'title':
            game_title = input("What is the game's title?: ")
            for line in f:
             # Iterate through each line in the file
                if game_title in line:
                    # Check if the game title is in the current line
                    new_line = line.split(",")
                    # Split the line into a list of values
                    string_line = ','.join(new_line)
                    # Join the list into a string with commas and print it
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
  

