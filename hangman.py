word = "sequoia" # This needs to be changed by the game owner as needed.
guess = "" # This is a variable where we'll be storing the player's correctly guesses letters.

attempts = 6

while attempts > 0: # This means that as long as the player doesn't reach 0 -they have 6 attempts!- the game can continue.
    guess_attempt = input("Please enter a letter: ") # We are asking the player to enter one letter.

    if guess_attempt in word:  # A conditional statement to define what happens if the letter is in the word or if it is not.
        print(f"Yay! {guess_attempt} is in the word.")
    else:
        attempts -= 1 # Because the player has 6 attempts, when they guess something wrong, the counter needs to decrease by 1.
        print(f"Oops.. {guess_attempt} is not in the word :( You have {attempts} attempts left!")

    guess = guess + guess_attempt # We are modifying the empty guess variable above by adding the correctly guessed letters.
    wrong_attempts = 0

    for i in word: # This loop is going to iterate through every letter in the given word.
        if i in guess:  # This would show the entire correct word if the guess and word variables match.
            print(f"{i}", end="")
        else:           # If the guess and word variables don't match, it will print dashes and the matching letters only.
            print("_", end="")
            wrong_attempts += 1 # This means that the wrong attempts will increase by one.
    print(" ")
    
    if wrong_attempts == 0: # This means that if the wrong attempts is 0, the player wins.
        print("Wow! You have guessed the word. You win ;)")
        break
else: # This is just in case the user never guesses the word.
    print(f"Try again later! The word was {word}")
