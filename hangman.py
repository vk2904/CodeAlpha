import random

def select_random_word(word_list):
    return random.choice(word_list)

def display_game_state(word, guessed_letters, incorrect_guesses, max_attempts):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Word: {display_word}")
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    print(f"Remaining attempts: {max_attempts - len(incorrect_guesses)}\n")

def get_player_guess(guessed_letters, incorrect_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
        elif guess in guessed_letters or guess in incorrect_guesses:
            print("You have already guessed that letter. Try again.")
        else:
            return guess

def play_hangman(word_list, max_attempts=6):
    word = select_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = []

    print("Welcome to Hangman!\n")
    
    while len(incorrect_guesses) < max_attempts:
        display_game_state(word, guessed_letters, incorrect_guesses, max_attempts)
        
        guess = get_player_guess(guessed_letters, incorrect_guesses)
        
        if guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                display_game_state(word, guessed_letters, incorrect_guesses, max_attempts)
                print("Congratulations! You've guessed the word correctly!")
                return
        else:
            incorrect_guesses.append(guess)
    
    print(f"Sorry, you've run out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    word_list = ["python", "apple", "challenge", "programming", "random","java"]
    play_hangman(word_list)
