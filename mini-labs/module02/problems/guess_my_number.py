import random

secret = random.randrange(1, 100)
attempts = 0
guess = None

print("Welcome to Guess My Number!\nTry to find the secret number")

while guess != secret:
    # 2.1 Ask user for a guess
    user_input = input("Submit your guess: ")

    # Convert input string to an integer
    guess = int(user_input)

    # 2.3 Increment the number of attempts
    attempts += 1
    # 2.2 Print a message with a hint
    if guess < secret:
        print("More!")
    elif guess > secret:
        print("Less!")

# 3. Print congratulations message with total attempts
print(f"Congratulations! You guessed the number in {attempts} attempt(s).")
