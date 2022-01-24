"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730407531"

word: str = input("Enter a 5-character word: ")
if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(character) < 1:
    print("Error: Character must be a single character.")
    exit()
counter: int = 0
print("Searching for " + character + " in " + word)

if word[0] == character:
    print(character + " found at index 0")
    counter = counter + 1
if word[1] == character:
    print(character + " found at index 1")
    counter = counter + 1
if word[2] == character:
    print(character + " found at index 2")
    counter = counter + 1
if word[3] == character:
    print(character + " found at index 3")
    counter = counter + 1
if word[4] == character:
    print(character + " found at index 4")
    counter = counter + 1

if counter == 0:
    print("No instances of " + character + " found in " + word)
if counter == 1:
    print("1 instance of " + character + " found in " + word)
if counter == 2:
    print("2 instances of " + character + " found in " + word)
if counter == 3:
    print("3 instances of " + character + " found in " + word)
if counter == 4:
    print("4 instances of " + character + " found in " + word)
if counter == 5:
    print("5 instances of " + character + " found in " + word)
