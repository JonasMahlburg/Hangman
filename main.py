import random

wordlist = ['Apple', 'Windows', 'Backend', 'Frontend', 'Python']





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

    while remaining_lives > 0:
        draw(word, guessed_letters)
        letter = input("Bitte trage einen Buchstaben ein: ").lower()

        if letter in guessed_letters:
            print("Diesen Buchstaben hast du schon versucht.")
            continue

        guessed_letters.append(letter)

        if letter not in word.lower():
            remaining_lives -= 1
            print(f"Falsch! Du hast noch {remaining_lives} Leben.")
        
        # Prüfe, ob alle Buchstaben erraten wurden
        if all(l.lower() in guessed_letters for l in word):
            print(f"Glückwunsch! Du hast das Wort '{word}' erraten.")
            break
    else:
        print(f"Game over! Das Wort war: {word}")


word = get_random_word(wordlist)
print("Willkommen zu Hangman")

game_loop(word)