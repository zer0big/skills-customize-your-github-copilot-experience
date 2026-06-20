"""Starter implementation for the Hangman game.

This file provides a clear, readable starting point for students.
Modify or extend functions to meet assignment requirements.
"""

import random
from typing import List


WORDS = ['python', 'hangman', 'challenge', 'programming', 'computer']


def choose_word(words: List[str]) -> str:
	return random.choice(words)


def display_progress(secret: str, guessed: set) -> str:
	return ' '.join([c if c in guessed else '_' for c in secret])


def is_word_guessed(secret: str, guessed: set) -> bool:
	return all(c in guessed for c in secret)


def main():
	secret = choose_word(WORDS)
	guessed = set()
	incorrect = set()
	max_incorrect = 6

	print("Welcome to Hangman! Guess letters to reveal the word.")

	while len(incorrect) < max_incorrect and not is_word_guessed(secret, guessed):
		print('\nWord: ', display_progress(secret, guessed))
		print(f"Incorrect guesses: {len(incorrect)}/{max_incorrect}")
		guess = input('Enter a single letter: ').strip().lower()
		if not guess or len(guess) != 1 or not guess.isalpha():
			print('Please enter a single alphabetic character.')
			continue
		if guess in guessed or guess in incorrect:
			print('You already tried that letter.')
			continue

		if guess in secret:
			guessed.add(guess)
			print('Good guess!')
		else:
			incorrect.add(guess)
			print('Wrong guess.')

	print('\nFinal word: ', secret)
	if is_word_guessed(secret, guessed):
		print('Congratulations — you guessed the word!')
	else:
		print('Out of attempts. Better luck next time!')


if __name__ == '__main__':
	main()

