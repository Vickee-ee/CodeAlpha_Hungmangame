import random

words = [
    "python", "javascript", "computer", "keyboard", "internet",
    "programming", "developer", "software", "hardware", "database",
    "algorithm", "function", "variable", "network", "security",
    "technology", "machine", "learning", "artificial", "intelligence",
    "robot", "science", "planet", "galaxy", "ocean", "mountain",
    "forest", "elephant", "tiger", "butterfly", "chocolate", "coffee",
    "football", "cricket", "bicycle", "camera", "telephone", "airport",
    "adventure", "mystery", "diamond", "thunder", "rainbow", "sunshine",
    "castle", "warrior", "dragon", "pirate", "rocket", "universe"
]

wordchoice = random.choice(words)
hiddenword = ["_"] * len(wordchoice)

lives = 5
guessed_letters = []

print("Welcome to Hangman!")
print("The word has", len(wordchoice), "letters.")
print(" ".join(hiddenword))

while lives > 0:

    user = input("Enter a letter: ").lower()

    if user in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(user)

    if user in wordchoice:

        for i in range(len(wordchoice)):
            if wordchoice[i] == user:
                hiddenword[i] = user

        print("Correct!")

    else:
        lives -= 1
        print("Wrong guess!")

    print("Word:", " ".join(hiddenword))
    print("Lives:", lives)

    if "_" not in hiddenword:
        print("You WIN!")
        print("The word was:", wordchoice)
        break

else:
    print("GAME OVER!")
    print("The word was:", wordchoice)