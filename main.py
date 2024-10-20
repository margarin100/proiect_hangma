import csv
from collections import deque

def read_and_solve(file_path):
    total_attempts = 0
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            game_code, masked_word, full_word = row
            attempts = automated_guess(masked_word, full_word)
            total_attempts += attempts
            print(f"Game Code: {game_code}, Attempts: {attempts}, Word: {full_word}")

    print(f"\nTotal Attempts for all games: {total_attempts}")

def automated_guess(masked_word, full_word):
    guessed_letters = set()  # Set pentru literele deja ghicite
    letter_attempts = 0  # Contorizăm numărul de încercări
    letter_priority = deque(['E', 'A', 'I', 'O', 'U',
                             'R', 'N', 'T', 'S', 'L',
                             'C', 'D', 'P', 'M', 'F', 'V', 'Z',
                             'B', 'G', 'H', 'J', 'X', 'Q', 'W', 'K', 'Ș', 'Ț'])

    # Set pentru literele care deja sunt descoperite în cuvântul mascat
    discovered_letters = set(masked_word) - {'*'}

    while masked_word != full_word and letter_priority:
        # Alegem următoarea literă din lista de priorități
        guess = letter_priority.popleft()

        # Dacă litera a fost deja ghicită sau este descoperită, o ignorăm
        if guess in guessed_letters or guess in discovered_letters:
            continue

        # Adăugăm litera la setul de litere ghicite
        guessed_letters.add(guess)
        letter_attempts += 1

        # Dacă litera ghicită este în cuvântul complet
        if guess in full_word:
            # Actualizăm cuvântul mascat doar cu literele noi corecte
            new_masked = list(masked_word)  # Transformăm într-o listă pentru modificare
            for idx, letter in enumerate(full_word):
                if letter == guess:
                    new_masked[idx] = guess  # Înlocuim asteriscul cu litera corectă
            masked_word = ''.join(new_masked)  # Refacem string-ul mascat

    return letter_attempts  # Returnăm numărul de încercări pentru acest joc



read_and_solve('cuvinte.txt')