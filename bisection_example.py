
"""
This code is a number guessing game. It prompts the user to think of a number between 0 and 100, 
and then uses a binary search algorithm to guess the number. The program keeps guessing until the 
user indicates that the guess is correct. It provides options for the user to indicate if the guess 
is too high or too low. Once the correct number is guessed, the program displays the secret number 
and ends the game.
"""
print("Please think of a number between 0 and 100!")

low = 0
high = 100
guess = (high + low)//2

while True:
    print("Is your secret number " + str(guess) + "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_input == 'h':
        high = guess
    elif user_input == 'l':
        low = guess
    elif user_input == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
    
    guess = (high + low)//2