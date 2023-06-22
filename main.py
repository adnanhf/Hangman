import random

#Step 1 
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
choosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter: ').lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in choosen_word:
  if letter == guess:
    print('Right')
  else:
    print('Wrong')

#Step 2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display.
for position in range(word_length):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replaced with "_".
#Hint - Don't worry about getting the user to guess the following letter. We'll tackle that in step 3.
print(display)
	
