import random
from wonderwords import RandomWord

print("----Welcome to the HANGMAN GAME-----")
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
stages_of_man = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

r = RandomWord()
chosen_word = r.word()

user_word = ""
word = []
for i in range(len(chosen_word)):
    user_word += "_"
    word.append("_")
print(user_word)
lives = 6
end_of_the_game = False
while not end_of_the_game:
    guess = input("guess a letter : ").lower()
    if guess in word:
        print("You have already guessed the word")

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            word[index] = letter
    print(f"{''.join(word)}")
    if "_" not in word:
        print("YOU WON!!!<3")
        break
    if guess not in chosen_word:
        print(stages_of_man[lives - 1])
        lives -= 1
        if lives == 0:
            print("YOU LOOSE:(")
            end_of_the_game = True
print(f"The word is {chosen_word}")
