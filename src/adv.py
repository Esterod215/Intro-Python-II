from room import Room
from player import Player
import textwrap

# Declare all the rooms


    
    

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# wrapper = textwrap.wrap(width=30)
# descriptionwrap
# Make a new player object that is currently in the 'outside' room.
userName = str(input("Enter Character's name\n"))
player1 = Player(userName,"outside")
userInput = 1


# Write a loop that:
while not userInput == 5:
    print(f"{player1.name}'s' current location: {room[player1.currentRoom].name}")
    print(room[player1.currentRoom])
    userInput = int(input("What do you want to do: [1] Move North [2] Move East [3] Move West [4] Move South [5] Quit\n"))

    if userInput == 1:
        if player1.checkMovement(1,room[player1.currentRoom].name):
            print("Moved North")
        else:
            print("Cannot move in this direction")

    
    elif userInput == 2:
        if player1.checkMovement(2,room[player1.currentRoom].name):
            print("Moved East")
        else:
            print("Cannot move in this direction")
   
    elif userInput == 3:
        if player1.checkMovement(3,room[player1.currentRoom].name):
            print("Moved West")
        else:
            print("Cannot move in this direction")
    
    elif userInput == 4:
        if player1.checkMovement(4,room[player1.currentRoom].name):
            print("Moved South")
        else:
            print("Cannot move in this direction") 
    
    elif userInput == 5:
        print("Goodbye")

    else:
        print("Invalid Input")



# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

