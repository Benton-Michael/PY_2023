# Ask User if they want to play a game


def hide_phrase(text):
    hidden_phrase = ''
    for character in text:
        if character != ' ':
            hidden_phrase += '#'
        else:
            hidden_phrase += ' '
    return hidden_phrase

# Helper function, called inside another function
def play_hangman():
    turns = 10
    phrase = "Vailla Ice Ice Baby"
    is_guess_correct = False
    hidden_phrase = hide_phrase(phrase)
    print( hidden_phrase )

    while turns > 0 and hidden_phrase != phrase:
        print(f'You have {turns} guesses left. Do not waste them!')
        is_guess_correct = False
        guessed_character = input('What guessest thou')
        
        new_hidden_phrase = ''
        for index in range(len(phrase)):
            if phrase[index].lower() == guessed_character.lower():
                is_guess_correct = True
                new_hidden_phrase += phrase[index]
            else:
                new_hidden_phrase += hidden_phrase[index]
        if not is_guess_correct:
            turns -= 1
        hidden_phrase = new_hidden_phrase
        
        print(hidden_phrase)
    if not turns:
        print(f"Game Over LOSER!!! The correct answer was '{phrase}'")
    else:
        print ("Congratulations! You won the Game")
    # for character in phrase:
    #     if guessed_character == character:
    #         new_hidden_phrase += character
    #     else: 
    #         pass

# cat dog
# ### ###
    

# if x == 'y' or x == 'Y':
# x = input('Do you want to play a game Y/y')

while input('Do you want to play a game? Y/y').lower() == 'y':
    play_hangman()

    # Challenge is to modify this code to use a list of phrases