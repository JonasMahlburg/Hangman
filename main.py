import random

wordlist = ["apple", "windows", "backend", "frontend", "python"]

wordlistCas = ["haus", "auto", "erdbeere", "hund", "katze"]


def display_hangman(remaining_lives):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(stages[remaining_lives])


def get_random_word(wordlist):
    return random.choice(wordlist)


def player_turn():
    input("Bitte trage einen Buchstaben ein: ")


def draw(word, guessed_letters):
    for letter in word:
        if letter.lower() in guessed_letters:
            print(f"{letter} ", end="")
        else:
            print("_ ", end="")
    print()


def game_loop(word):
    guessed_letters = []
    remaining_lives = 0

    while remaining_lives <= 6:
        display_hangman(remaining_lives)
        draw(word, guessed_letters)
        letter = input("Bitte trage einen Buchstaben ein: ").lower()

        if letter in guessed_letters:
            print("Diesen Buchstaben hast du schon versucht.")
            continue

        guessed_letters.append(letter)

        if letter not in word.lower():
            remaining_lives += 1
            print(f"Falsch! Du hast noch {remaining_lives} Leben.")

        # Prüfe, ob alle Buchstaben erraten wurden
        if all(L.lower() in guessed_letters for L in word):
            print(f"Glückwunsch! Du hast das Wort '{word}' erraten.")
            break
    else:
        print(f"Game over! Das Wort war: {word}")


word = get_random_word(wordlist)
print("Willkommen zu Developer-Hangman")

game_loop(word)
