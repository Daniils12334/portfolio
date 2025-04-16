import random
from wordslist import hangman_words

hangman_art = {
    0: """
       +---+
           |
           |
           |
          ===
    """,
    1: """
       +---+
       O   |
           |
           |
          ===
    """,
    2: """
       +---+
       O   |
       |   |
           |
          ===
    """,
    3: """
       +---+
       O   |
      /|   |
           |
          ===
    """,
    4: """
       +---+
       O   |
      /|\  |
           |
          ===
    """,
    5: """
       +---+
       O   |
      /|\  |
      /    |
          ===
    """,
    6: """
       +---+
       O   |
      /|\  |
      / \  |
          ===
    """
}

def display_man(wrong_guesses):
    print(hangman_art[wrong_guesses])

def display_hint(hint):
    print(" ".join(hint))

def main():
    difficulty = random.choice(["easy", "medium", "hard"])
    word = random.choice(hangman_words[difficulty])
   
    hint = ["_"] * len(word)
    wrong_guesses = 0
    guessed_letters = set()
    
    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        
        # Check win condition
        if "_" not in hint:
            print("Congratulations! You won!")
            print(f"The word was: {word}")
            break
            
        # Check lose condition
        if wrong_guesses >= 6:
            print("You lost!")
            print(f"The word was: {word}")
            break
            
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Letter I said!")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {6 - wrong_guesses} attempts left.")

if __name__ == "__main__":
    main()