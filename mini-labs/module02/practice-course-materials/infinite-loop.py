# Game loop prototype: an infinite loop
# runs until 'Game Over' or Player wants to exit
# Show the usage of the 'break' statement

while(True):
    user_input = input("Input:")
    print("Take inputs from the user")
    print("Update the game state")
    print("Render the game")
    if(user_input == 'q'):
        break

