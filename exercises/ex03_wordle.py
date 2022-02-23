"""Wordle."""

__author__ = "730407531"


def contains_char(word: str, char: str) -> bool:
    """Given a guessed word, returns a correct character contained."""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Given a guess and a secret word, return a string of emojis whose color codifies the same as EX02."""
    assert len(guess) == len(secret)
    i: int = 0
    counter: int = 0
    emoji_result: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    wrong_spot = False
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_result = emoji_result + GREEN_BOX
        else:
            wrong_spot = True
            while counter < len(secret):
                if secret[counter] == guess[i]:
                    emoji_result = emoji_result + YELLOW_BOX
                    counter = len(secret)
                    wrong_spot = True
                else:
                    counter = counter + 1
                    wrong_spot = False   
            if wrong_spot is False:
                emoji_result = emoji_result + WHITE_BOX
        counter = 0
        i = i + 1
    return emoji_result


def input_guess(exp_len: int) -> str:
    """Given an integer "expected length" of a guess, will prompt user for a guess until they guess a word of the appropriate length."""
    wordle_guess: str = input(f"Enter a {exp_len} character word: ")
    while len(wordle_guess) != exp_len:
        if len(wordle_guess) < exp_len:
            wordle_guess = input(f"That wasn't {exp_len} chars! Try again: ")
        if len(wordle_guess) > exp_len:
            wordle_guess = input(f"That wasn't {exp_len} chars! Try again: ")
    if len(wordle_guess) == exp_len:
        return wordle_guess
    return wordle_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    secret_word: str = "codes"
    win_game: bool = False

    while turns < 7 and win_game is False:
        print(f"=== Turn {str(turns)}/6 ===")
        guess = input_guess(len(secret_word))
        emoji_result = emojified(guess, secret_word)
        print(emoji_result)
        if guess == secret_word:
            print(f"You won in {turns}/6 turns! ")
            win_game = True
        else:
            turns = turns + 1
    if win_game is False:
        print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()