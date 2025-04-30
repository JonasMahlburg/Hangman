import random
import json
from wordlists import wordlist
from stages import stages


def display_hangman(remaining_lives):
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
    remaining_lives = 6

    with open("leaderboard.json", "r") as file:
        board = json.load(file)
    # sorted_board = sorted(board)
    print(board)

    while remaining_lives > 0:
        display_hangman(remaining_lives)
        draw(word, guessed_letters)
        letter = input("Bitte trage einen Buchstaben ein: ").lower()

        if letter in guessed_letters:
            print("Diesen Buchstaben hast du schon versucht.")
            continue

        guessed_letters.append(letter)

        if letter not in word.lower():
            remaining_lives -= 1
            print(f"Falsch! Du hast noch {remaining_lives} Versuche.")

        # Prüfe, ob alle Buchstaben erraten wurden
        if all(L.lower() in guessed_letters for L in word):
            print(f"Glückwunsch! Du hast das Wort '{word}' erraten.")
            name = input("ich brauche deinen Namen fürs Leaderboard: ")
            board[name] = remaining_lives

            with open("leaderboard.json", "w") as file:
                json.dump(board, file, indent=4)
          

            print("\nLeaderboard:")
            sorted_board = sorted(board.items(), key=lambda x: x[1], reverse=True)
            for i, (name, score) in enumerate(sorted_board, start=1):
                print(f"{i}. {name}: {score}")


            break
    else:
        print(f"Game over! Das Wort war: {word}")
        decision = input("möchtest du es nocheinmal probieren? [y/n]: ")

        if decision == "y":
            new_word = get_random_word(wordlist)
            print("Willkommen zu Developer-Hangman")
            game_loop(new_word)


word = get_random_word(wordlist)
print("Willkommen zu Developer-Hangman")

game_loop(word)
