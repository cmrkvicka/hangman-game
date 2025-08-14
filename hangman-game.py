print('--------------START SCRIPT--------------')

import pandas as pd


print('Welcome to my Hangman game!\n')
print('Guess one letter at a time, you get 6 mistakes before the game is over!\n')
print('If you want to end early, type \'quit\' and press enter')


mystery_phrase = 'KANGAROO'

blanks = ''
mistakes = 0

for letter in mystery_phrase:
    blanks = blanks + '_ '

print(blanks)

user_phrase = ''

mystery_phrase_dict = {}

for letter in mystery_phrase:
    mystery_phrase_dict[letter] = False

# print(mystery_phrase_dict)

user_guess = 'CCC'

revealed_phrase = ''

letters_guessed = set()

while True:

    user_guess = input('Guess a letter:').upper()
    print()
    
    if user_guess == 'QUIT':
        print('-----------------------')
        break
    if user_guess == 'CLAIRE':
        print('I LOVE YOU CLAIRE, YOU ARE THE LOVE OF MY LIFE,')
        print('LOVE CHARLIE <3333\n\n')
        print('-----------------------')
        continue
    if len(user_guess) != 1:
        print('Type only 1 letter please\n\n')
        continue

        #If guess is in the mystery phrase
    if mystery_phrase_dict.get(user_guess) != None:
        if mystery_phrase_dict.get(user_guess)==True:
            print('Guess a NEW letter maybe!\n\n')
            continue
        mystery_phrase_dict.update({user_guess: True})
        
        revealed_phrase = ''

        for letter in mystery_phrase:
            if mystery_phrase_dict.get(letter) == True:
                revealed_phrase = revealed_phrase + letter + ' '
            else:
                revealed_phrase = revealed_phrase + '_ '
        print(revealed_phrase + '\n\n')
    # If the guess is not in the mystery phrase
    else:
        if user_guess in letters_guessed:
            print('Guess a NEW letter maybe!\n\n')
        else:
            mistakes+=1
            if mistakes > 5:
                print('NOPE! Sorry you lose! Try again next time\n\n')
                break
            else:
                letters_guessed.add(user_guess)
                print('NOPE! Try again')
    
    print('Letters guessed: ', letters_guessed,'\n\n')
    print('Mistakes left: ',6-mistakes,'\n\n')
    print(revealed_phrase,'\n\n')

    #Check if game is won
    game_won = True
    for letter in mystery_phrase_dict:
        if mystery_phrase_dict[letter] == False:
            game_won = False
    
    if game_won == True:
        print('CONGRATS YOU WON!\n\n')
        break




    print('-----------------------')

print('--------------END SCRIPT--------------')