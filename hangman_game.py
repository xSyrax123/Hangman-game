#!/usr/bin/env python3
# Hangman game
from random import choice


class Hangman:
    HANGMAN_PICS = (r"""
        ┌───┐
        │   │
            │
            │
            │
            │
    ════════╛""", r"""
        ┌───┐
        │   │
        O   │
            │
            │
            │
    ════════╛""", r"""
        ┌───┐
        │   │
        O   │
        |   │
            │
            │
    ════════╛""", r"""
        ┌───┐
        │   │
        O   │
       /│   │
            │
            │
    ════════╛""", r"""
        ┌───┐
        │   │
        O   │
       /│\  │
            │
            │
    ════════╛""", r"""
        ┌───┐
        │   │
        O   │
       /│\  │
       /    │
            │
    ════════╛""", r"""
        ┌───┐
        │   │
        O   │
       /│\  │
       / \  │
            │
    ════════╛""")
    SPACER = "-" * 50

    def __init__(self, word):
        """Our constructor class that instantiates the game."""
        self.max_trials = len(self.HANGMAN_PICS) - 1
        self.trials = self.max_trials
        self.secret_word = word
        self.secret_word_low = word.lower()
        self.blanks = list("_" * len(self.secret_word))
        self.used_letters = set() 

    @property
    def _blanks_string(self):
        """Returns a string with blanks."""
        return "".join(self.blanks)

    @property
    def _draw_hangman(self):
        """Returns a string with the current position of the hangman."""
        return f"{self.HANGMAN_PICS[self.max_trials-self.trials]}\n"

    @property
    def _has_won(self):
        """Asigns a boolean value of True if the user guess the secret word."""
        return self._blanks_string == self.secret_word_low
    
    def _is_valid_input(self, letter):
        """Return True if the input is a single letter in the alphabet."""
        return len(letter) == 1 and letter.isalpha()

    def _guess_letter(self, letter):
        """Replace the guessed letter in the blanks where it matches in the
        secret word and return True if that letter appeared in the secret word.
        """
        good_guess = False
        for i, char in enumerate(self.secret_word_low):
            if char == letter:
                good_guess = True
                self.blanks[i] = letter
                self.used_letters.add(letter)
        return good_guess

    def play(self):
        """The game stage."""
        print(f"\nSecret word ({len(self.secret_word)} letters): {self._blanks_string}")
        print(self._draw_hangman)

        while self.trials > 0 and not self._has_won:
            print(self.SPACER)

            letter = input("\nEnter a letter: ").lower()

            if not self._is_valid_input(letter):
                print("The value entered is invalid.\n")
                continue

            if letter in self.used_letters:
                print("This letter has already been entered. Enter another letter.\n")
                continue

            guess_was_good = self._guess_letter(letter)
            self.used_letters.add(letter)

            if guess_was_good:
                print(f"{self._blanks_string}\n")
            else:
                self.trials -= 1
                print(f"You missed and lost a life. You have {self.trials} trials left.")
                print(self._draw_hangman)
                    
        if self._has_won:
            print(f"You won. The secret word was: {self.secret_word}.")
        else:
            print(f"You lost. The secret word was: {self.secret_word}.")
            

def main():
    """Selects a word from a list of words.
    This word is to be guessed in the game.
    """
    with open("words.txt", "r+", encoding="UTF-8") as words:
        secret_word = choice(words.read().split())
        secret_word = "".join(secret_word)
    game = Hangman(secret_word)
    game.play()


if __name__ == "__main__":
    main()
