import random  # For picking a random number

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)  # Random number between 1 and 100
    tries = 0  # Count how many guesses
    
    while True:
        try:
            guess = int(input("Enter your guess: "))  # Take user input
            tries += 1  # Increase tries by 1
            if guess < number:
                print("Too low, try again.")
            elif guess > number:
                print("Too high, try again.")
            else:
                print(f"Well done! You guessed it in {tries} tries.")
                break  # Exit loop when guessed right
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    guess_the_number()
