import matplotlib.pyplot as plt
from database import *
rentals = {}

def load_rentals():
    with open('Rental.txt') as f:
        for line in f:
            data = line.split(',')
            game_id = data[0]
            # Check if the game ID is already in the rentals dictionary
            if game_id in rentals:
                rentals[game_id] += 1
                # Increment the rental count for the game
            else:
                rentals[game_id] = 1
                # Add the game ID to the dictionary with a count of 1
           

def plot_frequency(): 
    # Get the game IDs and rental frequencies for plotting 
    ids = rentals.keys()
    frequencies = rentals.values()
    # Create a bar chart
    plt.bar(ids, frequencies)
    # Customize the plot
    plt.xticks(rotation=45)
    plt.xlabel('Game ID')
    plt.ylabel('Times Rented')
    plt.title('Rental Frequency')
    plt.style.use('dark_background')
    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()
   
load_rentals()
print(rentals.keys())
plot_frequency()


