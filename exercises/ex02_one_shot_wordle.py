
__author__ = "730407531"


secret_word: str = f"python"
guess: str = input(f"What is your 6-letter guess? ")
counter: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji_result: str = ""
wrong_spot: bool = False
alt_index: int = 0

while counter < len(guess):
    if guess[counter] == secret_word[counter]:
        emoji_result = emoji_result + GREEN_BOX
    else:
        wrong_spot = True
        while alt_index < len(secret_word):
            if secret_word[alt_index] == guess[counter]:
                emoji_result = emoji_result + YELLOW_BOX
                alt_index = 6
                wrong_spot = True
            else:
                alt_index = alt_index + 1
                wrong_spot = False    
        if wrong_spot == False:
            emoji_result = emoji_result + WHITE_BOX
    alt_index = 0
    counter = counter + 1
print(emoji_result)

while guess:
    if len(guess) < 6:
        guess = input("That was not 6 letters! Try again: ")
    if len(guess) > 6:
        guess = input("That was not 6 letters! Try again: ")
    if len(guess) == 6:
        if guess == secret_word:
            print("Woo! You got it!")
        else:
            print("Not quite. Play again soon!")
    exit()
